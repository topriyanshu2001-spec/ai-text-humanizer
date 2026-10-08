#!/usr/bin/env python3
"""Render a PRISMA 2020-style search and selection flow diagram.

    python3 make_prisma.py                      # uses counts.json, writes to ./out
    python3 make_prisma.py --counts my.json --out figures/

Design rules this enforces, because they are what reviewers check:

* Only INDEPENDENT counts are supplied. Records screened, reports sought, reports
  assessed and studies included are DERIVED here, so the figure cannot contradict
  itself.
* Any derived value that comes out negative means the inputs are inconsistent. The
  script names the failing equation and refuses to draw. A flow diagram whose
  numbers do not reconcile is the fastest way to lose a reviewer's confidence.
* Nulls mean "search not yet run". The script refuses rather than drawing zeros,
  so an unfilled template cannot be mistaken for a result.

Output: vector PDF, SVG and EPS, plus 600 dpi PNG and TIFF. Journals want vector;
the raster copies are for manuscript-embedding previews.

Typeface is Liberation Serif, which is metrically identical to Times New Roman. If
your journal demands the literal font and you have it installed, change FONT below.
"""
from __future__ import annotations

import argparse
import json
import sys
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

FONT = "Liberation Serif"   # metrically identical to Times New Roman
INK = "#000000"
BODY_PT = 8.6
PHASE_PT = 9.4


# --------------------------------------------------------------------- loading
def load(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        sys.exit(f"counts file not found: {path}")
    except json.JSONDecodeError as exc:
        sys.exit(f"counts file is not valid JSON: {exc}")
    return data


def unfilled(node, trail="") -> list[str]:
    """Every path whose value is still null."""
    out = []
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("_"):
                continue
            out += unfilled(v, f"{trail}.{k}" if trail else k)
    elif node is None:
        out.append(trail)
    return out


def total(section: dict) -> int:
    return sum(v for k, v in section.items() if not k.startswith("_"))


# ------------------------------------------------------------------ arithmetic
class Flow:
    """Derives every dependent count and checks each stays non-negative."""

    def __init__(self, c: dict):
        self.errors: list[str] = []

        self.db_total = total(c["databases"])
        self.reg_total = total(c["registers"])
        self.identified = self.db_total + self.reg_total

        rb = c["removed_before_screening"]
        self.dup = rb["duplicate_records"]
        self.auto = rb["marked_ineligible_by_automation"]
        self.other_removed = rb["removed_for_other_reasons"]
        self.removed_before = self.dup + self.auto + self.other_removed

        self.screened = self._check(
            self.identified - self.removed_before,
            "records screened = records identified − records removed before screening",
            f"{self.identified} − {self.removed_before}",
        )

        sc = c["screening"]
        self.excluded_ta = sc["records_excluded_at_title_abstract"]
        self.sought = self._check(
            self.screened - self.excluded_ta,
            "reports sought for retrieval = records screened − records excluded",
            f"{self.screened} − {self.excluded_ta}",
        )

        self.not_retrieved = sc["reports_not_retrieved"]
        self.assessed = self._check(
            self.sought - self.not_retrieved,
            "reports assessed for eligibility = reports sought − reports not retrieved",
            f"{self.sought} − {self.not_retrieved}",
        )

        self.ft_reasons = {k: v for k, v in c["full_text_exclusions"].items()
                           if not k.startswith("_")}
        self.ft_total = sum(self.ft_reasons.values())
        self.included_db = self._check(
            self.assessed - self.ft_total,
            "studies included via databases = reports assessed − reports excluded",
            f"{self.assessed} − {self.ft_total}",
        )

        # ---- other-methods arm
        self.other_sources = {k: v for k, v in c["other_methods"].items()
                              if not k.startswith("_")}
        self.other_identified = sum(self.other_sources.values())
        self.other_not_retrieved = c["other_methods_screening"]["reports_not_retrieved"]
        self.other_assessed = self._check(
            self.other_identified - self.other_not_retrieved,
            "other-methods reports assessed = records identified − not retrieved",
            f"{self.other_identified} − {self.other_not_retrieved}",
        )

        self.other_reasons = {k: v for k, v in c["other_methods_full_text_exclusions"].items()
                              if not k.startswith("_")}
        self.other_ft_total = sum(self.other_reasons.values())
        self.included_other = self._check(
            self.other_assessed - self.other_ft_total,
            "studies included via other methods = reports assessed − reports excluded",
            f"{self.other_assessed} − {self.other_ft_total}",
        )

        self.included_total = self.included_db + self.included_other
        self.reports_included = c["included"]["reports_of_included_studies"]

        if self.reports_included < self.included_total:
            self.errors.append(
                "reports of included studies "
                f"({self.reports_included}) is fewer than studies included "
                f"({self.included_total}); a study has at least one report"
            )

    def _check(self, value: int, equation: str, shown: str) -> int:
        if value < 0:
            self.errors.append(f"{equation}\n      gives {shown} = {value}, which is impossible")
        return value


# ----------------------------------------------------------------------- draw
#
# Layout engine. Boxes size themselves to their content, and every box is placed
# from a running cursor, so nothing can overlap by construction. Long labels wrap
# to the width of their column band.

LINE = 0.0190          # vertical space per text line, in axes fraction
VPAD = 0.0130          # padding above and below the text inside a box
GAP = 0.052            # vertical gap between stacked boxes


def wrap(lines, width):
    """Wrap each label to `width` characters, keeping continuation lines indented."""
    out = []
    for ln in lines:
        if len(ln) <= width:
            out.append(ln)
            continue
        out.extend(textwrap.wrap(ln, width=width, subsequent_indent="   ") or [ln])
    return out


class Box:
    def __init__(self, ax, x, w, top, lines, chars, *, pt=BODY_PT):
        self.lines = wrap(lines, chars)
        self.h = len(self.lines) * LINE + 2 * VPAD
        self.x, self.w = x, w
        self.top = top
        self.bottom = top - self.h
        self.mid_y = top - self.h / 2
        ax.add_patch(Rectangle((x, self.bottom), w, self.h, facecolor="white",
                               edgecolor=INK, linewidth=0.8))
        ax.text(x + 0.010, self.mid_y, "\n".join(self.lines), ha="left", va="center",
                fontsize=pt, family=FONT, color=INK, linespacing=1.42)

    @property
    def cx(self):
        return self.x + self.w / 2

    @property
    def right(self):
        return self.x + self.w


def arrow(ax, x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                 mutation_scale=9, linewidth=0.8,
                                 color=INK, shrinkA=0, shrinkB=0))


def phase(ax, y_top, y_bot, label):
    h = y_top - y_bot
    ax.add_patch(Rectangle((0.006, y_bot), 0.030, h,
                           facecolor="#ececec", edgecolor=INK, linewidth=0.8))
    ax.text(0.021, y_bot + h / 2, label, ha="center", va="center", rotation=90,
            fontsize=PHASE_PT, family=FONT, color=INK)


def render(f: Flow, c: dict, out: Path, stem: str, two_column: bool):
    if two_column:
        fig_w, fig_h = 13.0, 9.6
        MX, MW, CH = 0.072, 0.252, 46     # main band (databases arm)
        EX, EW, EC = 0.348, 0.208, 36     # its exclusion band
        OX, OW, OC = 0.580, 0.198, 34     # other-methods band
        XX, XW, XC = 0.792, 0.202, 34     # its exclusion band
    else:
        fig_w, fig_h = 9.0, 9.6
        MX, MW, CH = 0.105, 0.400, 58
        EX, EW, EC = 0.560, 0.410, 58
        OX = OW = OC = XX = XW = XC = None

    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

    db = [f"{k} (n = {v:,})" for k, v in c["databases"].items() if not k.startswith("_")]
    reg = [f"{k} (n = {v:,})" for k, v in c["registers"].items() if not k.startswith("_")]

    ax.text(MX, 0.982, "Identification of studies via databases and registers",
            ha="left", va="center", fontsize=PHASE_PT, family=FONT, color=INK)
    if two_column:
        ax.text(OX, 0.982, "Identification of studies via other methods",
                ha="left", va="center", fontsize=PHASE_PT, family=FONT, color=INK)

    top = 0.952
    b_id = Box(ax, MX, MW, top, ["Records identified from:"] + db + reg, CH)
    b_rm = Box(ax, EX, EW, top,
               ["Records removed before screening:",
                f"Duplicate records removed (n = {f.dup:,})",
                f"Records marked as ineligible by automation tools (n = {f.auto:,})",
                f"Records removed for other reasons (n = {f.other_removed:,})"], EC)
    arrow(ax, b_id.right, b_id.mid_y, b_rm.x, b_id.mid_y)
    id_bottom = min(b_id.bottom, b_rm.bottom)
    phase(ax, top + 0.012, id_bottom - 0.010, "Identification")

    y = id_bottom - GAP
    b_scr = Box(ax, MX, MW, y, [f"Records screened (n = {f.screened:,})"], CH)
    b_exc = Box(ax, EX, EW, y, [f"Records excluded (n = {f.excluded_ta:,})"], EC)
    arrow(ax, b_id.cx, b_id.bottom, b_id.cx, b_scr.top)
    arrow(ax, b_scr.right, b_scr.mid_y, b_exc.x, b_scr.mid_y)

    y = min(b_scr.bottom, b_exc.bottom) - GAP
    b_sgt = Box(ax, MX, MW, y, [f"Reports sought for retrieval (n = {f.sought:,})"], CH)
    b_nrt = Box(ax, EX, EW, y, [f"Reports not retrieved (n = {f.not_retrieved:,})"], EC)
    arrow(ax, b_scr.cx, b_scr.bottom, b_scr.cx, b_sgt.top)
    arrow(ax, b_sgt.right, b_sgt.mid_y, b_nrt.x, b_sgt.mid_y)

    y = min(b_sgt.bottom, b_nrt.bottom) - GAP
    b_asd = Box(ax, MX, MW, y, [f"Reports assessed for eligibility (n = {f.assessed:,})"], CH)
    b_fte = Box(ax, EX, EW, y,
                [f"Reports excluded (n = {f.ft_total:,}):"] +
                [f"{k} (n = {v:,})" for k, v in f.ft_reasons.items()], EC)
    arrow(ax, b_sgt.cx, b_sgt.bottom, b_sgt.cx, b_asd.top)
    arrow(ax, b_asd.right, b_asd.mid_y, b_fte.x, b_asd.mid_y)
    scr_bottom = min(b_asd.bottom, b_fte.bottom)
    phase(ax, id_bottom - 0.014, scr_bottom - 0.010, "Screening")

    o_bottom = scr_bottom
    if two_column:
        other = [f"{k} (n = {v:,})" for k, v in f.other_sources.items()]
        o_id = Box(ax, OX, OW, top, ["Records identified from:"] + other, OC)
        y_o = min(o_id.bottom, b_scr.top)
        o_sgt = Box(ax, OX, OW, b_sgt.top,
                    [f"Reports sought for retrieval (n = {f.other_identified:,})"], OC)
        o_nrt = Box(ax, XX, XW, b_sgt.top,
                    [f"Reports not retrieved (n = {f.other_not_retrieved:,})"], XC)
        arrow(ax, o_id.cx, o_id.bottom, o_id.cx, o_sgt.top)
        arrow(ax, o_sgt.right, o_sgt.mid_y, o_nrt.x, o_sgt.mid_y)

        o_asd = Box(ax, OX, OW, b_asd.top,
                    [f"Reports assessed for eligibility (n = {f.other_assessed:,})"], OC)
        o_exc = Box(ax, XX, XW, b_asd.top,
                    [f"Reports excluded (n = {f.other_ft_total:,}):"] +
                    [f"{k} (n = {v:,})" for k, v in f.other_reasons.items()], XC)
        arrow(ax, o_sgt.cx, o_sgt.bottom, o_sgt.cx, o_asd.top)
        arrow(ax, o_asd.right, o_asd.mid_y, o_exc.x, o_asd.mid_y)
        o_bottom = min(scr_bottom, o_asd.bottom, o_exc.bottom)

    y = o_bottom - GAP - 0.012
    b_inc = Box(ax, MX, MW, y,
                [f"Studies included in review (n = {f.included_total:,})",
                 f"Reports of included studies (n = {f.reports_included:,})"], CH)
    arrow(ax, b_asd.cx, b_asd.bottom, b_asd.cx, b_inc.top)
    if two_column:
        arrow(ax, o_asd.cx, o_asd.bottom, o_asd.cx, b_inc.mid_y)
        arrow(ax, o_asd.cx, b_inc.mid_y, b_inc.right, b_inc.mid_y)
    phase(ax, scr_bottom - 0.014, b_inc.bottom - 0.010, "Included")

    foot_y = b_inc.bottom - 0.045
    ax.text(MX, foot_y,
            f"Search last executed {c['meta']['search_last_executed']}.  "
            f"Screening: {c['meta']['screeners']}.  "
            f"Deduplication: {c['meta']['deduplication_tool']}.",
            ha="left", va="center", fontsize=7.6, family=FONT, color=INK)
    if c["meta"].get("review_type") == "narrative":
        ax.text(MX, foot_y - 0.028,
                "Search and selection flow for a critical narrative review, "
                "reported in the style of PRISMA 2020. This review was not "
                "registered and is not presented as a systematic review.",
                ha="left", va="center", fontsize=7.6, family=FONT,
                color=INK, style="italic")

    out.mkdir(parents=True, exist_ok=True)
    written = []
    for ext in ("pdf", "svg", "eps"):
        p = out / f"{stem}.{ext}"
        fig.savefig(p, bbox_inches="tight", facecolor="white")
        written.append(p)
    for ext in ("png", "tiff"):
        p = out / f"{stem}.{ext}"
        # LZW keeps the TIFF lossless but a fraction of the uncompressed size;
        # journals that ask for TIFF at 600 dpi accept LZW.
        kw = {"pil_kwargs": {"compression": "tiff_lzw"}} if ext == "tiff" else {}
        fig.savefig(p, dpi=600, bbox_inches="tight", facecolor="white", **kw)
        written.append(p)
    plt.close(fig)
    return written


# ------------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--counts", default="counts.json", type=Path)
    ap.add_argument("--out", default="out", type=Path)
    ap.add_argument("--stem", default="Figure_S1_PRISMA_flow")
    ap.add_argument("--layout", choices=["two-column", "single"],
                    default="two-column",
                    help="two-column includes the other-methods arm")
    args = ap.parse_args()

    c = load(args.counts)

    blanks = unfilled({k: v for k, v in c.items() if k != "_README"})
    if blanks:
        print("REFUSING TO RENDER — these counts are still empty:\n", file=sys.stderr)
        for b in blanks:
            print(f"  {b}", file=sys.stderr)
        print("\nRun the searches in search_strategy.md and record what they return.",
              file=sys.stderr)
        print("A flow diagram is a record of work done; it cannot be filled in from a template.",
              file=sys.stderr)
        sys.exit(2)

    f = Flow(c)
    if f.errors:
        print("REFUSING TO RENDER — the counts do not reconcile:\n", file=sys.stderr)
        for e in f.errors:
            print(f"  * {e}", file=sys.stderr)
        print("\nReviewers check this arithmetic first. Fix the inputs.", file=sys.stderr)
        sys.exit(3)

    files = render(f, c, args.out, args.stem, args.layout == "two-column")

    print("Flow reconciles:")
    print(f"  identified {f.identified:,}  (databases {f.db_total:,} + registers {f.reg_total:,})")
    print(f"  − removed before screening {f.removed_before:,}  → screened {f.screened:,}")
    print(f"  − excluded at title/abstract {f.excluded_ta:,}  → sought {f.sought:,}")
    print(f"  − not retrieved {f.not_retrieved:,}  → assessed {f.assessed:,}")
    print(f"  − excluded at full text {f.ft_total:,}  → included via databases {f.included_db:,}")
    print(f"  + included via other methods {f.included_other:,}")
    print(f"  = studies included {f.included_total:,} "
          f"({f.reports_included:,} reports)")
    print("\nWritten:")
    for p in files:
        print(f"  {p}")


if __name__ == "__main__":
    main()
