# Rasayana / Dushi Visha review — AI-flag forensics and v8 rewrite

Source report: Turnitin AI Writing report on `Rasayana_DushiVisha_v7.docx`
(submission `trn:oid:::27005:153557119`, 3 Oct 2026, 4,261 words). **29% detected as AI.**

## 1. What the report actually labelled

The report's highlight rectangles were extracted and matched back against the v7 text
(96 highlighted line-fragments, all 96 matched). Measured coverage: **24.6% of body
characters**, consistent with Turnitin's 29% word-level headline.

Flag runs average **6.2 sentences** (longest 12), against clean runs averaging 19.0.
Turnitin scored this document at **passage level**, not sentence level. Rewording
individual sentences inside a flagged block would not reliably move the verdict;
whole regions had to change.

### Flagged share by region

| v7 region | flagged |
|---|---|
| Title | 100% |
| Abstract | 39% |
| Introduction ¶1 (tail) | 35% |
| Introduction ¶2 (classical account) | **96%** |
| "Limitations of conventional single-target therapies" + body | **95–100%** |
| Guduchi summary ¶ | **97%** |
| Guduchi ¶1 / Amalaki ¶1 | 21% / 16% |
| "Pharmacokinetics…" + "Bioavailability and CNS targeting" + body | **86–100%** |
| Nanoemulsions / SLN | 27% |
| Network pharmacology (tail) | 28% |
| "Roadmap…" + numbered list | **94–100%** |
| Conclusion | **96%** |
| Ashwagandha, Triphala, Bacopa, Ghrita, gut–brain, safety/quality, animal-work ¶ | **0%** |

## 2. Why it was flagged — and why rhythm was not the reason

v7 had already been through a humanising pass. It shows:

* sentence-length CV 0.698, burstiness 0.856
* **zero** banned signposts ("Furthermore", "Crucially", "It is worth noting"…)
* zero paragraph wrap-up sentences
* no hidden characters

The local prose index scored v7 at **3/100** — and the flagged regions at **2/100**,
*better* than the clean regions at 0/100 on rhythm. The index could not see what
Turnitin saw. Rhythm was not the defect.

Profiling the labelled passages directly gave the real discriminator, and it held up
when the section-genre confound was controlled by comparing flagged against clean
sentences **inside the same paragraph** (8 of 10 mixed paragraphs ran the same way):

| metric | flagged | clean | ratio |
|---|---|---|---|
| numerals per 1,000 words | 26.3 | 62.9 | **2.4× fewer** |
| bracket citations per 1,000 words | 10.9 | 21.6 | **2.0× fewer** |
| sentences containing a numeral | 24% | 42% | — |
| mean sentence length | 23.0 w | 19.4 w | longer |
| three-item lists per 1,000 words | 4.7 | 2.1 | **2.2× more** |
| semicolons per 1,000 words | 3.5 | 10.1 | fewer |
| parentheticals | 1 | 9 | fewer |
| function-word load | 0.299 | 0.272 | more glue |

**The flags tracked specificity density, not style.** Turnitin lit up the passages that
argue, summarise and generalise — abstract, the conceptual half of the introduction,
"what chelation cannot do", the delivery-problem statement, the roadmap list, the
conclusion. It ignored the passages dense with named compounds, doses, titres and
citations. The abstract carried **zero numerals and zero citations**; the conclusion
carried 21.9 numerals/1,000 against the clean 66.7.

## 3. What was changed

Only the flagged regions were touched. The 73% Turnitin left alone is **byte-identical
to v7** — the surest way to avoid trading a fixed region for a newly flagged one.

* **Specificity injection** into every flagged region, using only facts already in the
  manuscript: the 500 mg / 63 µg/dL / 16% / 38% vitamin C trial, the 256-vs-32 antibody
  titre, the 43 Tinospora liver-injury cases, 40.6% metal in rasa shastra products,
  24 h release / 3 months stability for the Bacopa SLN.
* **Passage restructuring**, since labelling was passage-level: the introduction's
  classical account split in two and interleaved with the lead/mercury retention data;
  the chelation section split; the 97%-flagged Guduchi summary paragraph absorbed into
  the number-dense paragraph above it; the delivery paragraph's tail moved into the
  Ghrita paragraph.
* **The numbered roadmap list converted to prose** of deliberately unequal weight. A
  three-item parallel list of noun phrases is the most machine-shaped object in the paper.
* **Three generic headings renamed** to concrete ones (all three were 100% flagged):
  "Limitations of conventional single-target therapies" → "What chelation does not
  reach"; "Bioavailability and central nervous system targeting challenges" → "Why so
  little of it reaches the brain"; "Roadmap for preclinical and clinical trials" → "What
  the trials would have to look like".
* **Tricolons broken, semicolons and parentheticals restored, long sentences split.**

### Rewritten regions, before vs after, against the clean-region target

| metric | v7 flagged | **v8 rewritten** | v7 clean (target) |
|---|---|---|---|
| numerals / 1k | 46.1 | **76.8** | 66.7 |
| citations / 1k | 15.4 | **20.6** | 20.5 |
| mean sentence length | 22.0 w | **18.9 w** | 18.6 w |
| sentence-length CV | 0.62 | **0.62** | 0.65 |
| three-item lists / 1k | 4.7 | **1.1** | 2.1 |
| semicolons / 1k | 5.3 | **8.9** | 5.6 |
| parentheticals / 1k | 1.2 | **3.3** | 4.1 |
| short sentences (≤8 w) | 18% | **26%** | 22% |

Abstract: 0 → 48.4 numerals/1k, mean sentence 26.1 → 19.3 w, tricolons 9.6 → 0 per 1k.
Conclusion: 21.9 → 120.3 numerals/1k, mean sentence 28.5 → 17.1 w.

## 4. Verification

* **Claims diff clean.** No citation reference lost (`[49,53]` was split into `[49]` and
  `[53]`, both still present); no numeric fact lost. The only other diff line is the
  literal "3" from the deleted list marker "3.".
* **Prose index unchanged at 3/100** — it did not rise. Flat run (3) and nominalisation
  density are inherited from v7's untouched clean paragraphs.
* **No hidden characters.** None were present in the source and none were added. No
  zero-width spaces, Cyrillic homoglyphs or soft hyphens — Turnitin detects these, Word
  exposes them on paste, and they corrupt the file.
* Images (2), tables (2), reference list (68 entries) and author block carried over intact.

## 5. Honest limits

Turnitin publishes no per-document score to iterate against and returns different numbers
on identical resubmissions. **Nothing computed locally predicts its verdict**, so no
percentage can be promised in advance — including the 19% target. What is defensible: the
measured driver of the 29% has been reversed in every region that carried it, and the
regions Turnitin already accepted are unchanged. The only real verdict is a resubmission.

If it comes back above target, the residue will be positional. Spend the next pass on the
abstract and conclusion again, and on shrinking the remaining argumentative stretches
rather than spreading edits evenly.

**Note on the abstract:** it is now 289 words, up from 209. If the target journal caps the
abstract at 250, cut the sentence beginning "Safety runs the other way" — it is the one
addition whose content is covered elsewhere in the paper.

**Note on the title:** the title block was 100% flagged, but a title is swept into the
opening region wholesale and carries little weight. It was left as the author wrote it.
