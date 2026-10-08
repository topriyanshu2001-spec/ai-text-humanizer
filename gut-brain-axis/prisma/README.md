# PRISMA-style search and selection flow

Everything needed to produce a publication-quality flow diagram for the gut–brain review —
except the numbers, which can only come from running the searches.

## Why there are no numbers here yet

A flow diagram is a **record of work done**. Its whole function is to let a reader audit how a
pile of database hits became a set of included studies. Numbers that did not come from an
executed search are not a weak version of that; they are a fabrication, and in a Q1 submission
they are the kind that ends careers.

This container's network policy blocks PubMed, Embase, Scopus, Web of Science, Crossref,
OpenAlex and Semantic Scholar, so the searches cannot be run from here. The apparatus is built
and tested; you supply the counts.

Two ways to unblock:

- **Run the searches yourself.** `search_strategy.md` has the exact strings for each database.
  Paste, record the hit count, fill `counts.json`.
- **Widen network access.** Add those hosts under Allowed domains in the environment's Network
  access settings, and the searches can be executed and counted here.

## Files

| file | what it is |
|---|---|
| **`WORKSHEET.md`** | **start here.** Four queries to paste, ten numbers to write down, about fifteen minutes |
| `counts_minimal.json` | the short template the worksheet fills — ten numbers, no registers or automation fields |
| `search_strategy.md` | the full version: six databases, two registers, the other-methods arm, with every string spelled out |
| `counts.json` | the full template, if you ran the full search |
| `make_prisma.py` | validates the arithmetic, then renders the figure |
| `screening_log_template.csv` | per-record screening log, so exclusion counts are auditable |

## Use

```bash
pip install matplotlib pillow          # pillow is needed for the compressed TIFF
cd gut-brain-axis/prisma

# short route: WORKSHEET.md -> counts_minimal.json
python3 make_prisma.py --counts counts_minimal.json

# full route: search_strategy.md -> counts.json
python3 make_prisma.py

# layout is chosen automatically: the other-methods arm is dropped when it is
# empty. Force it either way with --layout two-column | single
```

Output lands in `out/`: vector **PDF, SVG and EPS**, plus **600 dpi PNG and LZW-compressed
TIFF**. Journals want the vector; the rasters are for embedding previews.

## Test renders mark themselves

A flow diagram drawn from invented numbers looks exactly like one drawn from real numbers. That
is a trap, so the script closes it: if the metadata still carries placeholder values — `TEST`,
`n/a`, `TBD`, `synthetic`, a bare `-` — it stamps **SYNTHETIC DATA / NOT FOR PUBLICATION**
diagonally across the figure and says on stderr which fields gave it away.

`--draft` forces the stamp. Real metadata never triggers it.

So a figure with no watermark is one you filled in yourself, from searches you ran.

## What the script refuses to do

Both refusals are deliberate, and both are what a reviewer checks first.

**It refuses to render an unfilled template.** Nulls mean "search not yet run", and it names
every field still empty rather than drawing zeros. An unfilled template cannot be mistaken for
a result.

**It refuses to render numbers that do not reconcile**, and names the failing equation:

```
REFUSING TO RENDER — the counts do not reconcile:

  * reports sought for retrieval = records screened − records excluded
      gives 180 − 900 = -720, which is impossible
```

You supply only **independent** counts. Records screened, reports sought, reports assessed and
studies included are **derived**, so the figure cannot contradict itself. If a derived value
goes negative, your inputs are inconsistent.

## The arithmetic it enforces

```
identified              = Σ databases + Σ registers
removed before screening = duplicates + automation-ineligible + other
records screened        = identified − removed before screening
reports sought          = records screened − records excluded
reports assessed        = reports sought − reports not retrieved
included via databases  = reports assessed − Σ full-text exclusion reasons

other-methods assessed  = Σ other sources − other not retrieved
included via other      = other assessed − Σ other exclusion reasons

studies included        = included via databases + included via other
reports of included studies ≥ studies included
```

## You may not need this figure at all

A critical narrative review is not expected to carry a PRISMA flow diagram. The convention —
the one the authors' own migraine review in this repository follows — is to report the search
in prose: databases, term blocks, date range, exclusions, how quality was judged. Section 2 of
the manuscript now does exactly that, and is complete once you insert the search date and
confirm which databases you used.

Treat this figure as polish. It adds transparency and some journals like it. It is not a
requirement, and skipping it costs the manuscript nothing.

## Typeface

Liberation Serif, metrically identical to Times New Roman. If your journal insists on the
literal font and you have it installed, change `FONT` at the top of `make_prisma.py`.

## A caution about what this diagram claims

The manuscript is a **critical narrative review**, and the figure says so in its footer:

> Search and selection flow for a critical narrative review, reported in the style of
> PRISMA 2020. This review was not registered and is not presented as a systematic review.

That sentence is load-bearing. A PRISMA flow diagram on an unregistered narrative review,
presented without qualification, invites a reviewer to ask for the PROSPERO number, the
pre-specified eligibility criteria, the dual-screening kappa and the risk-of-bias assessment —
none of which a narrative review has. Reported honestly, the same diagram is a credit: it shows
the search was systematic in execution even though the synthesis is interpretive.

If you later decide to convert the manuscript to a genuine systematic review, register with
PROSPERO **before** screening begins, not after. Retrospective registration is visible in the
record and reviewers treat it poorly.
