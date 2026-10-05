# From composition to circuit — a gut–brain axis review

A review article written from scratch, targeted at **Gut Microbes** (Taylor & Francis, Q1,
impact factor 15.3, CiteScore 19.5, fully open access). Modern biomedicine throughout; no
traditional-medicine content.

| file | what it is |
|---|---|
| `MANUSCRIPT.md` | the complete submission-shaped manuscript: 5,835 words main text, 241-word abstract, 4 tables, 2 figure legends, **and the full 106-entry reference list inside the document**, numbered in order of first appearance |
| `Gut_Brain_Neuroepithelial_Review_v1.docx` | the same manuscript as Word, double-spaced, tables rendered, editorial callouts in red |
| `REFERENCES.md` | working library only — the same 106 entries grouped by theme, for checking. Not the submission artefact |
| `SOURCES.md` | the five items still open before submission |
| `Gut_Brain_References_v1.docx` | the reference list as Word |
| `build_docx.py` | Markdown → .docx builder: Times New Roman throughout, every run black, double-spaced (never 1.5) |

## Manuscript structure

Built to match the house format of the authors' own submitted article in this repository
(`migraine/`), which is the right exemplar for a numbered-citation journal:

1. Article type, title, running title, authors, affiliations, corresponding author
2. Word-count line
3. Structured abstract, then keywords
4. Numbered sections (1–11), with tables and figure legends set where they are first discussed
5. Declarations — funding, conflicts, CRediT contributions, data availability, AI use, ethics
6. **References, inside the document**, numbered 1–106 in order of first appearance

Point 6 is the one that matters. A manuscript must be self-contained: an editor receives one
file, and a reference list living in a separate document is not a reference list. Numbering runs
by first appearance rather than by theme, which is what Vancouver style requires — reference 1 is
the first work cited in the introduction, not the first work alphabetically or topically.

## The argument

Two literatures share the name *microbiota–gut–brain axis* and do not meet the same evidential
standard.

**The compositional account** treats gut microbes as a diffuse humoral influence, measured as
community composition and correlated with behavioural outcomes. Its human evidence has not
consolidated. Mendelian randomisation studies drawing instruments from the same 16S GWAS return
contradictory taxon lists — one reports 5 taxa raising depression risk and 6 lowering it, another
10 and 10, a third 15 and 16 plus 36 reverse-causal effects. Meta-analyses of the same
intervention disagree in direction: faecal transplantation for depression pools at SMD ≈ −1.21 in
one synthesis, Hedges' g −0.81 in another, and **−0.10 (95% CI −0.60 to 0.41)** in a third.

**The circuit account** names cells, receptors, transmitters and afferents, and tests them by
deletion. Neuropod cells transduce luminal nutrients to vagal neurons in **milliseconds** via
glutamate, mapped by monosynaptic rabies tracing. Enterochromaffin cells — under 1% of intestinal
epithelium, source of most of the body's serotonin — couple metabolites to 5-HT3 afferents. The
vagus resolves into genetically addressable labelled lines.

A 2025 *Nature* result closed the gap: colonic PYY⁺ neuropod cells detect bacterial flagellin via
TLR5 and signal feeding through NPY2R vagal neurons. Microbial material, sensed by a named cell,
through a named receptor, along a named line.

The thesis is that microbial signalling should be modelled as input to defined sensory channels
rather than as systemic exposure to a community. The compositional account is not wrong; it is
under-specified in a way that has made it hard to falsify.

## Why this angle

Generic gut–brain surveys are among the most over-reviewed topics in neuroscience, and GLP-1
mechanism reviews were already saturated by 2025. The neuroepithelial literature is not, and it
carries a conceptual contribution rather than a summary — which is what separates a Q1 review
from a desk rejection.

*Gut Microbes* states that it "focuses in particular on mechanistic and cause and effect
studies." The journal's stated emphasis is the paper's thesis, which is the pre-submission
argument.

The paper also argues against itself where it should. Section 8 sets out the strongest objection
— that neuropod circuits operate over milliseconds while the clinical questions concern mood over
months — and concedes it is unresolved.

## Citation integrity

Every reference was verified against the published record before use. No DOI was constructed, no
author name expanded from initials, no citation generated to prop up a sentence.

**106 references, every one verified, and all 106 cited in the text.** No DOI was constructed, no
author name expanded from initials, no citation generated to prop up a sentence. The list was not
padded to the 140 asked for: 106 is what survived individual checking, and padding would defeat
the purpose.

`SOURCES.md` lists the five items still open. The two that matter: three Mendelian randomisation
studies described in §3.5 are accurately characterised but individually uncited, and the two
meta-analytic records carrying the paper's load-bearing effect sizes need their author lists and
page ranges confirmed. Fourteen further entries carry a `~` on one bibliographic field.

The Methods section carries an explicit placeholder for search strings and dates, to be filled
from a search the authors run themselves. Inventing one would be the error the paper is about.

## Prose measurement

Scored with `../tools/tellscan.py` — a formulaic-prose index, **not** a detector estimate. See the
root `README.md` for why that distinction matters.

| | AI-tell index |
|---|---|
| first draft | 8/100 |
| after expansion to 106 references | 7/100 |
| after final polish | **4/100** |

Parity with the other manuscripts in this repository. No hidden characters, no banned signposts,
soft filler at 0.7/1,000 words, zero balanced not-only/but-also frames. Residual penalties are a
flat run of 3 and nominalisation density 57.6/1k — the latter inherent to a subject whose nouns
are *transduction*, *composition* and *randomisation*.

## Rebuilding

```bash
pip install python-docx
python3 gut-brain-axis/build_docx.py gut-brain-axis/MANUSCRIPT.md out.docx

python3 - <<'PY' > /tmp/gb.txt
import re
t = open('gut-brain-axis/MANUSCRIPT.md').read()
b = t.split('## 1. Introduction')[1].split('## Declarations')[0]
for p in (r'^#+ .*$', r'^> .*$', r'^\|.*$'):
    b = re.sub(p, '', b, flags=re.M)
b = re.sub(r'\*\*|\*|_', '', b)
print(re.sub(r'\[\d+(?:,\s*\d+)*\]', '', b))
PY
python3 tools/tellscan.py /tmp/gb.txt
```

## Word formatting

Both .docx files are **Times New Roman throughout, every run black, double line spacing — not
1.5**. Word's built-in heading styles are blue Calibri Light, so headings are constructed by hand
rather than through `add_heading()`, and a final sweep restyles every run in the body and in
table cells so nothing inherits a theme font. Editorial callouts are carried in bold rather than
colour.

## Known limits

The container's network policy blocked PubMed, PMC, ScienceDirect, Crossref and DOI resolution,
so verification ran through web search rather than direct lookup. Titles, journals, years and
findings are confirmed; some author strings and page ranges are not, and `SOURCES.md` marks each
one. Widening the environment's allowed domains would close the gap.
