#!/usr/bin/env python3
"""tellscan.py - measures structural fingerprints of LLM prose. NOT a detector score.
Stdlib only.  python3 tellscan.py draft.txt [--json|--claims]"""

import sys, re, math, json
from collections import Counter

S = lambda t: [x for x in t.split("|") if x]

HARD_BAN = S("""furthermore|moreover|additionally|consequently|paradoxically|notably|importantly|
crucially|ultimately|overall,|in conclusion|to conclude|in summary|to summarize|in essence|
it is worth noting|it is important to note|it is essential to|it should be noted|it is crucial to|
one must consider|delve|delves|delving|tapestry|realm|myriad|plethora|underscore|underscores|
underscoring|pivotal|paramount|cornerstone|testament to|multifaceted|intricate|nuanced interplay|
showcase|showcases|seamless|seamlessly|robust framework|holistic approach|comprehensive understanding|
profound implications|ever-evolving|rapidly evolving|in the realm of|in the landscape of|
navigate the complexities|shed light on|shedding light on|plays a vital role|plays a crucial role|
plays a significant role|serves as a|stands as a|at the forefront of|a growing body of|
the intersection of|unlock the potential|harness the power|revolutionize|game-changer|cutting-edge|
state-of-the-art|invaluable|indispensable|unparalleled|remarkable potential|
warrants further investigation|further research is needed|holds promise|promising avenue|
avenue for future research|bridging the gap|paving the way|sets the stage""".replace("\n", ""))

SOFT_BAN = S("""significant|significantly|various|numerous|several studies|recent studies|
emerging evidence|leverage|leveraging|foster|fostering|facilitate|utilize|utilization|encompass|
encompasses|vital|essential|key factor|crucial|enhance|enhanced|enhancement|optimal|effective|
efficacy of|landscape|framework|paradigm|synergy|synergistic|in today's|in modern|increasingly|
widely recognized|well-established|extensively studied""".replace("\n", ""))

WRAPUP = S("""thus|therefore|hence|overall|in short|taken together|collectively|together, these|
these findings|this suggests|this highlights|this demonstrates|this underscores|this reflects|
such findings|in this way|as such|ultimately""".replace("\n", ""))

BALANCED = [r"\bnot only\b[^.]{0,80}\bbut also\b", r"\bboth\b[^.]{0,60}\band\b",
            r"\branging from\b[^.]{0,60}\bto\b", r"\bwhether\b[^.]{0,60}\bor\b"]

ABBREV = (r"(?:et al|i\.e|e\.g|cf|vs|viz|approx|Fig|Figs|Tab|Eq|Ref|No|Dr|Prof|Mr|Mrs|Ms|St|Jr|Sr|"
          r"Inc|Ltd|ca|p|pp|ed|eds|vol|min|max|sp|spp|subsp|var|wt|conc|temp|inj)\.")

INVISIBLE = dict(zip("​‌‍﻿⁠­᠎⁡⁢⁣⁤͏",
    S("ZERO WIDTH SPACE|ZWNJ|ZWJ|BOM|WORD JOINER|SOFT HYPHEN|MONGOLIAN SEP|FUNCTION APP|"
      "INVISIBLE TIMES|INVISIBLE SEP|INVISIBLE PLUS|GRAPHEME JOINER")))
HOMOGLYPH = dict(zip("аеорсхуіјοΑΒΕΟ",
    S("CYR a|CYR e|CYR o|CYR p|CYR c|CYR x|CYR y|CYR i|CYR j|GRK omicron|GRK Alpha|GRK Beta|"
      "GRK Epsilon|GRK Omicron")))

UNIT = (r"%|percent|mg/kg|g/kg|mL/kg|ng/mL|pg/mL|ug/mL|mcg/mL|IU/L|U/L|U/mg|w/w|v/v|mg|kg|ug|mcg|"
        r"ng|pg|uM|mM|nM|pM|mL|L|IU|fold|h|hr|hrs|min|sec|days?|weeks?|months?|years?|x")

# ------------------------------------------------------------------ parsing

def paragraphs(t): return [p.strip() for p in re.split(r"\n\s*\n", t) if p.strip()]

def sentences(block):
    p = re.sub(ABBREV, lambda m: m.group(0).replace(".", "\x00"), block)
    p = re.sub(r"\b([A-Z])\.", lambda m: m.group(1) + "\x00", p)
    p = re.sub(r"(\d)\.(\d)", lambda m: m.group(1) + "\x00" + m.group(2), p)
    out = []
    for s in re.split(r"(?<=[.!?])[\"')\]]*\s+", p):
        s = s.replace("\x00", ".").strip()
        if len(re.findall(r"[A-Za-z]", s)) >= 3: out.append(s)
    return out

def words(s): return re.findall(r"[A-Za-z][A-Za-z'\-]*", s)
def mean(x): return sum(x) / len(x) if x else 0.0
def stdev(x):
    if len(x) < 2: return 0.0
    m = mean(x); return math.sqrt(sum((v - m) ** 2 for v in x) / (len(x) - 1))
def entropy(c):
    n = sum(c.values())
    return -sum((v / n) * math.log2(v / n) for v in c.values() if v) if n else 0.0

# ------------------------------------------------------------------ metrics

def analyse(text):
    paras = paragraphs(text)
    sents, pc = [], []
    for p in paras:
        ss = sentences(p); pc.append(len(ss)); sents.extend(ss)
    if len(sents) < 3: sys.exit("Need at least 3 sentences to scan.")

    lens = [len(words(s)) for s in sents]
    aw = words(text); nw = len(aw)
    k = lambda n: round(n * 1000 / nw, 2) if nw else 0.0
    low = text.lower(); M = {}

    M["cv"] = round(stdev(lens) / mean(lens), 3) if mean(lens) else 0.0
    d = [abs(lens[i] - lens[i - 1]) for i in range(1, len(lens))]
    M["burstiness"] = round(mean(d) / mean(lens), 3) if mean(lens) else 0.0

    run = best = 1
    for i in range(1, len(lens)):
        a, b = lens[i - 1], lens[i]
        run = run + 1 if a and abs(a - b) / a <= 0.25 else 1
        best = max(best, run)
    M["flat_run"] = best

    M["short_per_100w"] = round(sum(1 for l in lens if l <= 8) * 100 / nw, 2)
    M["long_count"] = sum(1 for l in lens if l >= 32)
    M["mean_len"] = round(mean(lens), 1); M["min_len"] = min(lens); M["max_len"] = max(lens)

    hard = [(t, low.count(t)) for t in HARD_BAN if t in low]
    soft = [(t, len(re.findall(r"\b" + re.escape(t) + r"\b", low))) for t in SOFT_BAN]
    soft = [(t, c) for t, c in soft if c]
    M["hard_hits"] = sorted(hard, key=lambda x: -x[1]); M["hard_total"] = sum(c for _, c in hard)
    M["soft_hits"] = sorted(soft, key=lambda x: -x[1])[:12]
    M["soft_per_1k"] = k(sum(c for _, c in soft))

    M["tricolon_n"] = len(re.findall(r"\b[\w\-]+,\s+[\w\-][^,.;:]{0,40},\s+and\s+", text))
    M["tricolon_per_1k"] = k(M["tricolon_n"])
    M["emdash_n"] = text.count("—") + text.count("–") + len(re.findall(r"\s--\s", text))
    M["emdash_per_1k"] = k(M["emdash_n"])

    M["punct_entropy"] = round(entropy(Counter(
        c for c in text if c in ",;:()?!—–")), 3)
    M["semicolons"] = text.count(";"); M["questions"] = text.count("?"); M["parens"] = text.count("(")

    op = [words(s)[0].lower() for s in sents if words(s)]
    M["opener_diversity"] = round(len(set(op)) / len(op), 3)
    r = br = 1
    for i in range(1, len(op)):
        r = r + 1 if op[i] == op[i - 1] else 1; br = max(br, r)
    M["opener_repeat_run"] = br; M["top_openers"] = Counter(op).most_common(4)
    M["the_this_openers"] = round(sum(1 for o in op if o in
        ("the", "this", "these", "it", "in", "while", "however", "by", "as")) / len(op), 3)

    M["para_sent_counts"] = pc
    M["para_cv"] = round(stdev(pc) / mean(pc), 3) if len(pc) > 1 and mean(pc) else 0.0

    wl = [w.lower() for w in aw]; f = Counter(wl)
    M["hapax_ratio"] = round(sum(1 for c in f.values() if c == 1) / len(f), 3) if f else 0.0
    M["nominal_per_1k"] = k(sum(1 for w in wl if len(w) > 6 and
        re.search(r"(tion|sion|ment|ance|ence|ity|ness|ization|isation)s?$", w)))

    wraps = []
    for p in paras:
        ss = sentences(p)
        if len(ss) >= 2:
            tail = ss[-1].lower()
            if any(tail.startswith(c) or tail.startswith("and " + c) for c in WRAPUP):
                wraps.append(ss[-1][:60])
    M["wrapup_n"] = len(wraps); M["wrapup_examples"] = wraps[:3]
    M["balanced_n"] = sum(len(re.findall(p, low)) for p in BALANCED)
    M["passive_per_1k"] = k(len(re.findall(
        r"\b(is|are|was|were|be|been|being)\s+(\w+ed|\w+en)\b", low)))

    M["invisible_chars"] = {INVISIBLE[c]: text.count(c) for c in INVISIBLE if c in text}
    M["homoglyphs"] = {HOMOGLYPH[c]: text.count(c) for c in HOMOGLYPH if c in text}
    M["n_words"] = nw; M["n_sents"] = len(sents); M["_lens"] = lens; M["_sents"] = sents
    return M

# ------------------------------------------------------------------ scoring

CHECKS = [  # key, label, direction, target, weight
 ("cv",               "sentence-length variation (CV)",     "min", 0.60, 14),
 ("burstiness",       "adjacent-sentence burstiness",       "min", 0.50, 12),
 ("flat_run",         "longest flat run of sentences",      "max", 2,    10),
 ("short_per_100w",   "short sentences per 100 words",      "min", 0.45, 9),
 ("hard_total",       "banned signposts / fingerprints",    "max", 0,    14),
 ("soft_per_1k",      "soft filler per 1000 words",         "max", 6.0,  6),
 ("tricolon_per_1k",  "three-item lists per 1000 words",    "max", 3.0,  5),
 ("emdash_per_1k",    "em-dashes per 1000 words",           "max", 4.0,  5),
 ("punct_entropy",    "punctuation entropy (bits)",         "min", 1.30, 5),
 ("opener_diversity", "distinct sentence openers",          "min", 0.70, 6),
 ("the_this_openers", "share of generic openers",           "max", 0.42, 5),
 ("para_cv",          "paragraph-length variation",         "min", 0.32, 5),
 ("hapax_ratio",      "hapax ratio (lexical surprise)",     "min", 0.55, 6),
 ("nominal_per_1k",   "nominalizations per 1000 words",     "max", 48.0, 4),
 ("wrapup_n",         "paragraph wrap-up sentences",        "max", 0,    8),
 ("balanced_n",       "balanced not-only/but-also frames",  "max", 1,    4),
]

def score(M):
    rows, pen, tot = [], 0.0, 0.0
    for key, label, dr, tgt, w in CHECKS:
        v = M[key]
        if dr == "min":
            ok = v >= tgt; miss = 0.0 if ok else min(1.0, (tgt - v) / tgt if tgt else 1.0)
        else:
            ok = v <= tgt; miss = 0.0 if ok else min(1.0, (v - tgt) / ((tgt or 1.0) * 1.6))
        pen += miss * w; tot += w
        rows.append((label, v, ("<=" if dr == "max" else ">=") + str(tgt), ok, round(miss * w, 1)))
    idx = round(100 * pen / tot)
    if M["invisible_chars"] or M["homoglyphs"]: idx = 100
    return idx, rows

BAR = "-" * 68

def report(M, idx, rows):
    print(BAR)
    print(f"  AI-TELL INDEX: {idx}/100     ({M['n_words']} words, {M['n_sents']} sentences)")
    print("  formulaic-prose measure, NOT a detector score")
    print(BAR)
    for label, v, tgt, ok, cost in rows:
        print(f"  [{'PASS' if ok else 'FAIL'}] {label:<36}{str(v):>7}  need {tgt:<6}"
              f"{'' if ok else '-' + str(cost)}")
    print(BAR)
    print(f"  rhythm: mean {M['mean_len']}w, range {M['min_len']}-{M['max_len']}, "
          f"flat run {M['flat_run']}, long sentences {M['long_count']}")
    print(f"  paragraphs: {M['para_sent_counts']}    passive/1k: {M['passive_per_1k']}")
    print(f"  punctuation: {M['semicolons']} semicolons, {M['parens']} parens, "
          f"{M['questions']} questions, {M['emdash_n']} dashes")
    print(f"  openers: {M['top_openers']}  (repeat run {M['opener_repeat_run']})")
    if M["hard_hits"]:
        print("  BANNED: " + ", ".join(f"{t} x{c}" for t, c in M["hard_hits"][:14]))
    if M["soft_hits"]:
        print("  filler: " + ", ".join(f"{t} x{c}" for t, c in M["soft_hits"][:10]))
    for w in M["wrapup_examples"]:
        print(f'  DELETE wrap-up: "{w}..."')
    if M["invisible_chars"] or M["homoglyphs"]:
        print(f"  !! HIDDEN CHARACTERS - STRIP, DO NOT SHIP: "
              f"{M['invisible_chars']} {M['homoglyphs']}")
    lens, sents = M["_lens"], M["_sents"]; mu = mean(lens)
    print("  most average-length (rewrite these first):")
    for i in sorted(sorted(range(len(lens)), key=lambda j: abs(lens[j] - mu))[:3]):
        print(f"     [{lens[i]}w] {sents[i][:70]}...")
    print(BAR)

def claims(text):
    """Every factual anchor a rewrite must not disturb. Diff before vs after."""
    out = set()
    for m in re.findall(r"\d+(?:\.\d+)?\s*-?\s*(?:" + UNIT + r")(?![A-Za-z])", text, re.I):
        out.add("NUM  " + re.sub(r"\s+", " ", m.strip().lower()))
    for m in re.findall(r"\b\d+(?:\.\d+)?\b", text):
        out.add("VAL  " + m)
    for m in re.findall(r"\b[A-Z][a-zA-Z\-]+\s+et\s+al\.?,?\s*\(?\d{4}\)?", text):
        out.add("CITE " + re.sub(r"\s+", " ", m.strip()))
    for m in re.findall(r"\[\d+(?:[,\-]\s*\d+)*\]", text):
        out.add("CITE " + m)
    for m in re.findall(
            r"\(([A-Z][a-zA-Z\-]+(?:\s+(?:and|&)\s+[A-Z][a-zA-Z\-]+)?"
            r"(?:\s+et\s+al\.?)?,?\s+\d{4}[a-z]?)\)", text):
        out.add("CITE (" + re.sub(r"\s+", " ", m.strip()) + ")")
    for m in re.findall(r"\b(?:[A-Z][a-z]+){2,}\b|\b[A-Z]{2,}(?:[\-/][A-Z0-9]+)*\b"
                        r"|\b[A-Z][a-z]+\s+[a-z]{4,}(?:ii|ae|um|us|is|a)\b", text):
        out.add("TERM " + m)
    return sorted(out)

def main():
    argv = sys.argv[1:]
    args = [a for a in argv if not a.startswith("--")]
    text = open(args[0], encoding="utf-8").read() if args else sys.stdin.read()
    if "--claims" in argv:
        print("\n".join(claims(text))); sys.exit(0)
    M = analyse(text); idx, rows = score(M)
    if "--json" in argv:
        M.pop("_lens"); M.pop("_sents")
        print(json.dumps({"index": idx, "metrics": M}, indent=2))
    else:
        report(M, idx, rows)
    sys.exit(0 if idx <= 12 else 1)

if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.stderr.close()
