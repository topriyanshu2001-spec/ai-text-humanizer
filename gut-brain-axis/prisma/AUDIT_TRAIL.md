# If a reviewer asks for proof

Four things can be demanded of a review's search. They differ enormously in what they cost you,
and three of the four you can satisfy today.

---

## 1. "Give us the exact search strings and the date"

**The most common request by far.** For a narrative review it is usually the only one.

**You have this.** `search_strategy.md` holds the complete strings for every database, written
to be pasted and re-run. Section 2 of the manuscript names the databases, the four term blocks
and the exclusions in prose.

**What you supply:** the month and year of your final search. That is the single field in
Section 2 still marked for completion.

**What satisfies them:** supply `search_strategy.md` as Supplementary File 1. A reviewer who
pastes your string and gets a comparable number of hits is satisfied. They do not expect an
identical count — databases change weekly — which is exactly why the date matters.

---

## 2. "Are these citations real?"

**You are in an unusually strong position here**, stronger than most submissions.

All 106 references were individually checked against the published record before entering the
manuscript. `REFERENCES.md` groups them by the section each supports. `SOURCES.md` records what
was verified and the nine entries where one bibliographic field still needs confirming.

The strongest single piece of evidence: the most-cited paper in the adjacent authentication
field — the 2013 *BMC Medicine* DNA barcoding study — was **retracted in July 2024**, and it was
caught and kept out. Reviews published after that retraction still cite it. Being able to say
"we ran a retraction check and here is what it caught" is a direct answer to the question.

**Do before submitting:** re-run a retraction sweep across all 106. Retraction Watch and the
Crossref `update-to` field take minutes.

---

## 3. "Provide the records and your screening decisions"

**This is the one you cannot produce retrospectively**, and the reason matters.

Database exports and screening logs are made *at the moment of searching*. Rebuilt afterwards
from the reference list, they are reconstructions, and a reviewer who asks for them is
precisely the kind who can tell.

**So capture the following when you run the searches, not later:**

| capture | how | why it matters |
|---|---|---|
| Result count per database | screenshot showing the query **and** the count together | the count is unreproducible later; databases change |
| Full record export | RIS or BibTeX, one file per database, filename carrying the date | this is the actual evidence; the count alone is an assertion |
| Deduplicated set | export after dedup, keep the tool and version | lets a reviewer reproduce your screened number |
| Screening decisions | `screening_log_template.csv`, one row per record | the only way to justify the exclusion reasons in the figure |
| Full-text exclusions with reasons | same file, reason column | the flow diagram's exclusion box must sum to these |

Keep them in a dated folder alongside the manuscript. If the journal offers a data repository,
deposit them and cite the DOI in the Methods — that converts "trust us" into a link.

There is a symmetry here worth noticing. The companion manuscript in this repository argues that
herb-induced liver injury cases are uninterpretable because nobody retained the product the
patient actually swallowed. A review whose records were never retained has the same problem, for
the same reason. Retention is cheap at the moment of collection and impossible afterwards.

---

## 4. "Add a PRISMA flow diagram"

**Read this request carefully, because it is usually asking for something larger than a figure.**

A PRISMA flow diagram belongs to a systematic review. If a reviewer asks a narrative review for
one, they are either (a) applying a template without noticing the article type, or (b) telling
you they want the review reclassified. Those need different answers.

### If you want to supply the figure

Run `WORKSHEET.md` — about fifteen minutes — and render. The figure is honest as long as its
footer stays: *"reported in the style of PRISMA 2020. This review was not registered and is not
presented as a systematic review."*

### If you want to decline

This is a legitimate response, and it is better made confidently than apologetically. Drafted
reply:

> We thank the reviewer for this suggestion. The manuscript is submitted as a critical narrative
> review rather than a systematic review, and we have taken care not to present it as the
> latter: no protocol was registered, no formal risk-of-bias instrument was applied, and no
> quantitative synthesis was attempted. PRISMA 2020 is a reporting guideline for systematic
> reviews and meta-analyses, and its authors note that it is not designed for other review
> types. Supplying a PRISMA flow diagram here would imply methodological commitments the review
> does not make.
>
> We have instead reported the search in full in Section 2, naming the databases, the term
> blocks with their controlled-vocabulary headings, the date range, the hand-searching and
> forward citation tracking, and the explicit exclusion criteria. The complete search strings
> are given in Supplementary File 1 so that any reader can re-run them. We would be glad to add
> a search and selection flow diagram, reported in the style of PRISMA 2020 and labelled as a
> narrative review flow, if the editor considers it useful.

That last sentence matters. Offering the figure on your own terms is stronger than refusing
outright, and it costs you fifteen minutes if they accept.

### If they want a genuine systematic review

Say so plainly and treat it as a different paper. It needs PROSPERO registration **before**
screening, pre-specified eligibility criteria, two independent screeners with an agreement
statistic, risk-of-bias assessment per included study, and the 27-item PRISMA checklist.
Retrospective registration is visible in the PROSPERO record and reviewers treat it poorly, so
there is no shortcut worth taking.

---

## What to have ready at submission

- [ ] Section 2 complete: search date inserted, database list confirmed
- [ ] `search_strategy.md` attached as Supplementary File 1
- [ ] Retraction sweep run across all 106 references
- [ ] The nine entries flagged in `SOURCES.md` confirmed at the journal page
- [ ] Reference 64 author list supplied — it currently reads `[AUTHOR LIST TO BE SUPPLIED]`
- [ ] If you ran searches: exports, dated count screenshots and screening log filed together
- [ ] If you rendered the figure: confirm it carries **no** synthetic-data watermark
