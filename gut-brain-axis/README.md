# From composition to circuit — a gut–brain axis review

A review article written from scratch, targeted at **Gut Microbes** (Taylor & Francis, Q1,
impact factor 15.3, CiteScore 19.5, fully open access). Modern biomedicine throughout; no
traditional-medicine content.

| file | what it is |
|---|---|
| `MANUSCRIPT.md` | the review: 4,454 words main text, 247-word abstract, 4 tables, 2 figure legends, 11 verified references |
| `Gut_Brain_Neuroepithelial_Review_v1.docx` | the same manuscript as Word, double-spaced, tables rendered, editorial callouts in red |
| `SOURCES.md` | verification log — per-reference status and the uncited claims that must be closed out |
| `build_docx.py` | Markdown → .docx builder (headings, tables, bold/italic, superscripts, red callouts) |

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

**The manuscript is not submission-ready, and `SOURCES.md` says exactly why.** Eleven cited
sources against the 80–150 a *Gut Microbes* review carries. More seriously, the meta-analytic
figures in §3.5 and Table 1 — the paper's most load-bearing numbers — were verified during
writing but their bibliographic records were not captured, so they currently stand uncited.
Quoting a pooled effect size without its citation is the exact failure the manuscript criticises.
Close that file out first.

The Methods section carries an explicit placeholder for search strings and dates, to be filled
from a search the authors run themselves. Inventing one would be the error the paper is about.

## Prose measurement

Scored with `../tools/tellscan.py` — a formulaic-prose index, **not** a detector estimate. See the
root `README.md` for why that distinction matters.

| | AI-tell index |
|---|---|
| first draft | 8/100 |
| after opener, punctuation and tricolon passes | **4/100** |

Parity with the other manuscripts in this repository. No hidden characters, no banned signposts,
soft filler at 0.25/1,000 words. Residual penalties are a flat run of 3, opener diversity 0.622
and nominalisation density 53.8/1k — the last inherent to a subject whose nouns are
*transduction*, *composition* and *randomisation*.

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

## Known limits

The container's network policy blocked PubMed, PMC, ScienceDirect, Crossref and DOI resolution,
so verification ran through web search rather than direct lookup. Titles, journals, years and
findings are confirmed; some author strings and page ranges are not, and `SOURCES.md` marks each
one. Widening the environment's allowed domains would close the gap.
