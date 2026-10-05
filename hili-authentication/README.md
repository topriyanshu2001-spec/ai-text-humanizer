# Causality without identity — a new Q1 review

A review article written from scratch, targeted at the *Journal of Ethnopharmacology*
(Elsevier, Q1, impact factor 5.4), on the gap between causality assessment and exposure
authentication in herb-induced liver injury.

Unlike the other two manuscripts in this repository, this one was not remediated from a flagged
draft. It was built new, and the measurement discipline was applied while writing rather than
afterwards.

| file | what it is |
|---|---|
| `MANUSCRIPT.md` | the review: 5,140 words main text, 249-word structured abstract, 4 tables, 2 figure legends, 18 verified references |
| `SOURCES.md` | verification log — per-reference status, uncited claims, the retraction catch, what the authors must close out |
| `COVER_LETTER.md` | drafted cover letter plus a pre-send checklist |

## The argument

Causality instruments score timing, dechallenge and competing causes. Every one of them assumes
the implicated agent is known. Traditional polyherbal products break that assumption four ways:
taxonomic substitution, polyherbal attributability, adulteration with metals or synthetic drugs,
and variability within an authentic species.

The paper's load-bearing evidence comes from the field's own investigators. When the *Tinospora
cordifolia* case-series authors retrieved material from patients and analysed it, **four of four
raw plant samples were identified** by morphology, microscopy, HPTLC and DNA barcoding, and
**neither of the two commercial preparations could be analysed at all**, because co-formulated
ingredients interfered. The limit is analytical reach, not clinician diligence — and it binds
precisely on the product formats patients actually buy.

The proposal is an identity-certainty axis (I0–I4) reported alongside causality, with sample
retention as its precondition. It restrains both sides: an I0 record cannot convict a plant, and
it cannot acquit one either.

## Why this topic

Three criteria drove the choice. Author authority — Agadtantra Evum Vidhivaidyak *is* Ayurvedic
toxicology and forensic medicine, so this is the authors' discipline rather than a reach.
An open gap — RUCAM's inability to substitute for herb authentication is stated in the primary
literature by the instrument's own architects and has never been addressed. And a live, contested
question, with an active 2026 frontier pairing chemical authentication with updated RUCAM.

Existing reviews here catalogue which herbs injure the liver. None interrogates the instrument.

## Citation integrity

Every reference was verified against the published record before entering the text. Nothing was
written from memory.

The check that mattered most: the field's most-cited evidence for herbal substitution — the 2013
*BMC Medicine* DNA barcoding study and its "59% of products" figure — was **retracted in July
2024** for data fabrication. It still circulates in reviews published after the retraction.
It is kept out of this manuscript's evidence base and appears only as a cited retraction.
Replacements came from Seethapathy et al. (2019), Ichim (2019) and Vassou et al. (2022).

`SOURCES.md` records what remains open. The draft is not submission-ready until that file is
closed out: several author strings and page ranges need confirming against journal pages, seven
statements need a citation attached, and the Methods section carries an explicit placeholder for
search dates the authors must supply from a search they actually run.

That placeholder is deliberate. Inventing a methods statement, or a PRISMA diagram for an unrun
search, would be the same category of error the paper is about.

## Prose measurement

Scored with `../tools/tellscan.py`, which is a formulaic-prose index and **not** a detector
estimate — see the root `README.md` for why that distinction matters.

| | AI-tell index |
|---|---|
| the Q1 writing guide that prompted this work | **100/100** |
| this manuscript, first draft | 13/100 |
| this manuscript, final | **4/100** |

The guide scored worst on the two variables it defines for the reader: burstiness 0.477 against
a 0.50 floor, sentence-length CV 0.432 against 0.60, and a flat run of 8. It also carried two
U+200B zero-width spaces, on the bullets for "Perplexity" and "Burstiness".

This manuscript carries no hidden characters, no banned signposts, zero soft filler, and sits at
parity with the two remediated manuscripts in this repository. Residual penalties are a flat run
of 3, opener diversity at 0.578, and nominalisation density at 58/1k — the last being inherent to
a subject whose core nouns are *authentication*, *adulteration* and *causality*. Grinding those
down would cost more in prose quality than the index is worth, and the root `README.md` is
explicit that this index has no demonstrated power to predict any detector.

## Rebuilding the measurement

```bash
python3 - <<'PY' > /tmp/prose.txt
import re
t = open('hili-authentication/MANUSCRIPT.md').read()
b = t.split('## 1. Introduction')[1].split('## Declarations')[0]
for p in (r'^#+ .*$', r'^> .*$', r'^\|.*$'):
    b = re.sub(p, '', b, flags=re.M)
b = re.sub(r'\*\*|\*|_', '', b)
print(re.sub(r'\[\d+(?:,\s*\d+)*\]', '', b))
PY
python3 tools/tellscan.py /tmp/prose.txt
python3 tools/tellscan.py /tmp/prose.txt --claims > /tmp/claims.txt
```

## Known limits

The container's network policy blocked PubMed, PMC, ScienceDirect, Crossref and DOI resolution,
so verification ran through web search rather than direct database lookup. Titles, journals,
years and findings are confirmed; some author strings and page ranges are not. `SOURCES.md` marks
each one. Widening the environment's allowed domains would close that gap for future work.
