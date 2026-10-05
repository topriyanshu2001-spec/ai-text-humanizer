# Open items before submission

The full verified reference library is in `REFERENCES.md` (106 entries, grouped by the section
each supports). Every entry was checked against the published record before admission; none was
written from memory, no DOI was constructed, and no author name was expanded from initials.

Every one of the 106 is cited in the text, and no citation in the text lacks a library entry.

This file lists what is **still open**. It is short, and it is not optional.

---

## 1. Three Mendelian randomisation studies, §3.5

The passage describes three MR studies reporting mutually contradictory taxon lists:

- five taxa positively and six negatively associated with depression
- ten protective and ten deleterious
- fifteen positive and sixteen negative, with thirty-six reverse-direction effects

All three were located during research and their findings are accurately described. **None is
individually cited**, because their full bibliographic records were not captured.

Two acceptable fixes. Either retrieve and cite all three, or rewrite the passage to describe the
pattern without quoting specific counts — for instance, "studies using overlapping instruments
report taxon lists that do not agree with one another, in direction as well as identity." The
second option costs the paragraph some force and is honest as it stands.

**Do not leave the counts in the text uncited.** Quoting three specific results without
attribution is precisely the failure the manuscript criticises two sections later.

## 2. Two meta-analytic records, §3.6 and Table 1

Reference [38] (*Nutr Rev* 2025;83(7):e1504) carries the probiotic pooled estimates: SMD −0.96
(95% CI −1.31 to −0.61), I² = 85%, the ~⅓ fall after excluding high risk-of-bias studies, and
the −0.53 (95% CI −0.67 to −0.39) figure. **Its author list was not confirmed.**

Reference [42] (*Front Psychiatry* 2026, Fu J et al.) carries the FMT null result: SMD −0.10
(95% CI −0.60 to 0.41) from seven studies in 235 participants. **Volume and article number were
not confirmed.** The Hedges' g −0.81 and SMD ≈ −1.21 estimates quoted alongside come from two
further FMT syntheses whose records were not captured; attribute them or drop them.

These are the manuscript's most load-bearing numbers. Confirm them first.

## 3. Fourteen entries with a `~` field

Marked individually in `REFERENCES.md`. In each case the paper and its finding are verified; a
volume, page range or full author list was not displayed in a verified search result. Each needs
a one-minute check at the journal page.

Entries affected: 15, 34, 38, 39, 42, 97, 103, 104, 105, 106, plus four where only the author
list is short.

## 4. Methods section placeholder, §2

`MANUSCRIPT.md` §2 carries a `[TO CONFIRM BEFORE SUBMISSION]` block. Database names, exact search
strings and the final search date must be filled in from a search the authors execute themselves.
They are not asserted in the draft, deliberately.

## 5. Retraction sweep

Run a retraction and expression-of-concern check across all 106 entries before submitting.
Retraction Watch and the Crossref `update-to` field are the quickest routes. This is cheap, and
it is the single highest-value remaining check — the companion manuscript in this repository
exists partly because the most-cited paper in *its* field turned out to be retracted.

---

## Environment constraint behind items 1–3

Verification ran in a container whose network policy denies `pubmed.ncbi.nlm.nih.gov`,
`pmc.ncbi.nlm.nih.gov`, `sciencedirect.com`, `api.crossref.org` and `doi.org`. Checking therefore
went through web search, one record at a time, rather than direct database or DOI resolution.

Adding those hosts under Allowed domains in the environment's Network access settings would
close items 1–3 and 5 in a handful of queries, with exact author strings, volumes, pages, PMIDs
and DOIs throughout.

## What was deliberately not done

- No citation was generated to support a sentence. Where no verified source existed, the claim is
  flagged here rather than dressed with a plausible-looking reference.
- The list was not padded to 140. One hundred and six is what survived individual checking.
- No PRISMA diagram, no registration, no screening counts. This is a critical narrative review
  and says so.
- No hidden characters. Checked for zero-width spaces, soft hyphens and Cyrillic or Greek
  homoglyphs: none present.
- No claim that the circuit account explains mood or cognition. §8 states the opposite and sets
  out the strongest objection to the paper's own thesis.
