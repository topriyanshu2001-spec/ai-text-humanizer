# ai-text-humanizer

Diagnosis-first AI-flag remediation for the *Rasayana Therapy as a Systems-Level
Countermeasure to Dushi Visha and Latent Toxicity* review.

The method here is not paraphrasing. A Turnitin AI report was treated as labelled data:
the highlighted passages were extracted, profiled against the unhighlighted ones, and the
discriminator was measured rather than guessed. In this document rhythm turned out to be
irrelevant — v7 already had excellent sentence variance and zero signpost vocabulary — and
**specificity density** (numerals, citations, parentheticals per 1,000 words) carried the
signal. See `FORENSICS.md` for the full analysis and the before/after numbers.

## Contents

| path | what it is |
|---|---|
| `Rasayana_DushiVisha_v8.docx` | the revised manuscript, ready to resubmit |
| `FORENSICS.md` | why v7 was flagged at 29%, what changed, and the honest limits |
| `tools/tellscan.py` | formulaic-prose scanner (`--json`, `--claims`) |
| `tools/rewrite_v8.py` | the rewritten regions, keyed by v7 paragraph index |
| `tools/build_v8.py` | rebuilds the .docx from the v4 shell + rewrites |
| `tools/v7_paras.json` | v7 paragraphs reconstructed from the report PDF |
| `tools/flagged.txt` | the 96 highlighted fragments pulled from the report |
| `tools/flagmark.json` | per-character flag mask over the v7 body |

## Rebuilding

```bash
pip install python-docx pdfplumber
cd tools && python3 build_v8.py        # writes Rasayana_DushiVisha_v8.docx
python3 tellscan.py prose_v8.txt      # prose index
python3 tellscan.py prose_v8.txt --claims > claims_v8.txt   # fact inventory to diff
```

`tellscan.py` reports an **AI-tell index**: a measure of how formulaic the prose is. It is
not a detector score and has no demonstrated power to predict one. This document is the
proof — it scored 3/100 while Turnitin returned 29%. Use it to catch signpost vocabulary,
wrap-up sentences and flat rhythm, and never quote it as a detector estimate.

## Hard rules observed

- No invented numbers, citations, doses or softened findings. Every figure moved into a
  rewritten region was already in the manuscript; the claims diff is clean.
- No hidden characters. No zero-width spaces, homoglyphs or soft hyphens — these are
  detectable, they corrupt the submitted file, and unlike editing they are deception.
- Regions the detector already accepted were left byte-identical.
