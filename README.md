# ai-text-humanizer

Diagnosis-first AI-flag remediation for two review manuscripts.

The method is not paraphrasing. Each Turnitin AI report is treated as labelled data: the
highlighted passages are extracted, matched back to the source, and profiled against the
unhighlighted ones, so the discriminator is measured rather than guessed.

**The two manuscripts needed different diagnoses, which is the main lesson here.**

| manuscript | Turnitin | what actually separated flagged from clean |
|---|---|---|
| Rasayana / Dushi Visha | 29% | **specificity density** — flagged passages carried 2.4× fewer numerals and 2× fewer citations (held up under a within-paragraph control) |
| Migraine / Ardhavabhedaka | 26% | **nothing measurable** — a 21-metric permutation battery found no separation surviving correction; flagged passages had *more* numerals and identical rhythm. The actionable finding was positional |

In neither case did rhythm matter. Both drafts already had strong sentence variance and zero
signpost vocabulary, and both scored 3/100 on the local prose index while Turnitin returned
26–29%. That is the central caveat about the scanner below.

## Contents

| path | what it is |
|---|---|
| `Rasayana_DushiVisha_v8.docx` | revised Rasayana manuscript, ready to resubmit |
| `FORENSICS.md` | why Rasayana v7 was flagged at 29%, what changed, honest limits |
| `migraine/Migraine_Beyond_CGRP_Ardhavabhedaka_Review_v2.docx` | revised migraine manuscript |
| `migraine/FORENSICS.md` | the migraine analysis, including the hypothesis that was tested and retired |
| `migraine/tools/` | its rewrite module, builder, parallelism metric and flag mask |
| `tools/tellscan.py` | formulaic-prose scanner (`--json`, `--claims`) |
| `tools/rewrite_v8.py` | the rewritten regions, keyed by v7 paragraph index |
| `tools/build_v8.py` | rebuilds the .docx from the v4 shell + rewrites |
| `tools/v7_paras.json` | v7 paragraphs reconstructed from the report PDF |
| `tools/flagged.txt` | the 96 highlighted fragments pulled from the report |
| `tools/flagmark.json` | per-character flag mask over the v7 body |

Each manuscript's `tools/` directory holds the flag mask and the rewrite module, so any claim in
either `FORENSICS.md` can be recomputed.

## Rebuilding

```bash
pip install python-docx pdfplumber
cd tools && python3 build_v8.py        # writes Rasayana_DushiVisha_v8.docx
python3 tellscan.py prose_v8.txt      # prose index
python3 tellscan.py prose_v8.txt --claims > claims_v8.txt   # fact inventory to diff
```

`tellscan.py` reports an **AI-tell index**: a measure of how formulaic the prose is. It is
not a detector score and has no demonstrated power to predict one. This document is the
proof: both manuscripts scored 3/100 while Turnitin returned 26% and 29%. Use it to catch
signpost vocabulary, wrap-up sentences and flat rhythm, and never quote it as a detector
estimate.

`migraine/tools/tmpl.py` adds a clause-parallelism measure (mean max Jaccard overlap of
function-word skeleton trigrams between clauses of the same paragraph). It is useful for finding
templated enumerations, but note that it did *not* separate flagged from clean text at p < 0.05
in the migraine manuscript — see that report.

## Hard rules observed

- No invented numbers, citations, doses or softened findings. Every figure moved into a
  rewritten region was already in the manuscript; the claims diff is clean.
- No hidden characters. No zero-width spaces, homoglyphs or soft hyphens — these are
  detectable, they corrupt the submitted file, and unlike editing they are deception.
- Regions the detector already accepted were left byte-identical.
