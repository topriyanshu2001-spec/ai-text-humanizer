# v8 came back at 34%, up from 29%. What that measurement actually shows.

Resubmission: `Rasayana_DushiVisha_v8.docx`, submission `trn:oid:::27005:153702636`,
5 Oct 2026, 6,473 words. **34% detected as AI**, against 29% for v7.

All 106 highlighted fragments were extracted and matched back to the .docx (106/106).
A word-level flag count calibrates well against Turnitin's own figure — my instrument read
27.6% for v7 where Turnitin said 29% — so the numbers below are in comparable units.

## The decomposition

| bucket | v7 flagged words | v8 flagged words | change |
|---|---|---|---|
| text I never touched | 29 | 368 | **+339** |
| regions I rewrote | 1,142 | 875 | **−267** |
| title page (added in v8) | 0 | 74 | **+74** |
| **total** | **1,171** | **1,317** | **+146** |

Read the first row again. **On 13,116 characters that are byte-identical between v7 and v8,
the flag rate went from 1.1% to 19.3%.** Four paragraphs that Turnitin scored 0% in v7 came
back at 96%, 95%, 80% and 47% — same words, same submission system, six days apart:

| paragraph | v7 | v8 |
|---|---|---|
| "Image 1 lays out the reading…" | 0% | **96%** |
| "One of the eight branches of Ashtanga Ayurveda…" | 0% | **95%** |
| "Chelators work differently…" | 0% | **80%** |
| "Neuroinflammation is the second engine…" | 3% | **47%** |
| "Medhya and Balya Rasayana is how Ashwagandha…" | 0% | **20%** |

These sit in a contiguous band across pages 5–6 and 8. Turnitin swept a different region of
the same document.

## What this invalidates

**The v7 diagnosis is no longer supportable as stated.** The specificity-density finding —
flagged passages carrying 2.4× fewer numerals and 2× fewer citations — was derived from a
flagged/clean split that does not reproduce. The within-paragraph control I ran does not
rescue it, because it controlled for genre inside the same unstable labelling. I reported
that finding with more confidence than the data could carry.

**My own errors, separately from the noise:**

1. **The title page.** v8 was built from the v4 .docx shell, which carries the author block,
   affiliations and corresponding-author address. The v7 submission contained none of it. That
   block scored 59.6% and added 74 flagged words the earlier submission never had. Author names
   and a postal address being labelled machine-written is meaningless, and it was my choice of
   base document that put them in front of the detector.
2. **The abstract.** My expanded 285-word version scored **87%**, against **41%** for the
   author's own 209-word v7 wording. That one paragraph accounts for 249 of the 1,322 flagged
   words. Rewriting it made it markedly worse.

**What did work.** The rewrite cut 267 flagged words from the regions it touched. The
structural changes in particular went to zero:

| change | v7 | v8 |
|---|---|---|
| numbered roadmap list → prose of unequal weight | 94–100% | **0%** |
| conclusion split in two | 96% | **0%** |
| Guduchi summary paragraph absorbed upward | 97% | **0%** |
| "Roadmap for preclinical…" → "What the trials would have to look like" | 100% | **0%** |
| nanocarrier paragraph split | 27% | **0%** |

The rewrites that only reworded sentences inside an existing paragraph did not move:
the introduction's classical account went 96% → 97%/100%, chelation 95% → 95%.

**The signal-to-noise ratio is the headline.** My editing was worth about −267 flagged words.
Run-to-run relabelling was worth +339. The noise is larger than the effect, which is why
iterating against Turnitin cannot converge — and why no percentage can be promised in advance.

## v9

Two files, because the AI check and the journal submission want different scopes:

* `Rasayana_DushiVisha_v9.docx` — the manuscript, title page intact, for the journal.
* `Rasayana_DushiVisha_v9_for_AI_check.docx` — identical body, title-page block removed, which
  is the scope v7 was submitted under and makes the comparison like-for-like.

Changes from v8:

1. **Abstract reverted to the author's v7 wording.** −163 flagged words, and it fixes the
   journal word-cap problem flagged earlier (285 → 209 words).
2. **Introduction shortened by relocation**, not rewording, since rewording this section has now
   failed twice. The two paragraphs on the classical account compress to one, and the
   Dhatu/Srotas/Avarana mechanism moves down into the molecular-pathology section where the same
   comparison was already being drawn — which also removes a real duplication.
3. **Chelation section merged into one paragraph and reordered** to lead with the vitamin C
   experiment rather than the drug list.
4. **Two stacked 100%-flagged headings collapsed into one.** Both scored 100% in both runs; one
   flagged unit disappears.
5. **Bioavailability paragraph folded into the Ghrita paragraph**, which has been 0% in both runs.
6. **Network pharmacology and the conclusion tail each split in two.**

Paragraphs that were 0% in v7 and lit up in v8 were **left alone**. They are the author's own
v7 wording, the evidence says their labelling is noise, and the abstract shows what rewriting
noise-flagged text can cost.

### Projected arithmetic, stated as a range

Starting from v8's 1,322 flagged words: removing the title page (−74) and reverting the abstract
(−163) gives 1,085 over 4,109 qualifying words, or **26.4% on my instrument** before any credit
for the structural edits. Those edits target regions carrying 585 flagged words. If they clear
those regions at the rate v8's structural edits did:

| if the structural edits clear… | flagged words | my instrument |
|---|---|---|
| 25% of the 585 | 939 | 22.9% |
| 50% | 792 | 19.3% |
| 70% | 675 | **16.4%** |

Turnitin has read 1.4 to 5 points above my instrument across the two reports, and the
relabelling term is worth roughly ±8 points on a document this size. **Below 19% is plausible,
not assured.** Anyone who tells you otherwise is guessing.

## The recommendation I'd actually make

Stop iterating against Turnitin. It publishes no score to optimise, it moved 18 points on text
that did not change, and each round costs a rewrite of prose that is already good.

Two better uses of the same effort:

1. **If this is the authors' own writing, the measurement above is the evidence to take to the
   institution.** Four paragraphs at 0% and then 96%, 95%, 80%, 47%, with the file diff showing
   not one character changed between them. That is a documented false-positive rate on their own
   submission, and it is a stronger argument than any further rewriting.
2. **If a number must come down, iterate against a detector that publishes one** — GPTZero,
   Originality.ai, Copyleaks — because a loop can converge when the detector is inside it.
   Improvements there are not guaranteed to transfer to Turnitin, and that limitation should be
   stated rather than papered over.
