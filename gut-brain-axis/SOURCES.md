# Verification log

Every reference in `MANUSCRIPT.md` was checked against the published record before it entered
the text. Nothing was written from memory, no DOI was constructed, and no author name was
expanded from initials. This file records what was confirmed, what was not, and what must be
closed out before submission.

## Environment constraint

Verification ran in a container whose network policy denied `pubmed.ncbi.nlm.nih.gov`,
`pmc.ncbi.nlm.nih.gov`, `sciencedirect.com`, `api.crossref.org`, `doi.org` and
`europepmc.org` (403 at the proxy). Checking therefore went through web search rather than
direct database or DOI resolution.

Consequence: **titles, journals, years and principal findings are confirmed; full author
strings, volume/page ranges and DOIs are confirmed only where a result displayed them.**
Fields marked `CONFIRM` need a short check against the journal page. Adding those hosts under
Allowed domains in the environment's Network access settings would remove the limit.

## Reference status

| # | Source | Verified | Status |
|---|---|---|---|
| 1 | Sudo N, Chida Y, Aiba Y, et al. *J Physiol* 2004;558(Pt 1):263–75 | Title, first author, journal, year, volume, pages; exaggerated HPA response reversed by *B. infantis*; reduced cortical/hippocampal BDNF | `CONFIRM` full author list |
| 2 | Valles-Colomer M, Falony G, Darzi Y, et al. *Nat Microbiol* 2019;4(4):623–32 | Title, authors, journal, volume, pages; *Coprococcus*/*Dialister* depletion; Flemish Gut Flora Project n≈1,054 with independent validation | Verified |
| 3 | Kaelberer MM, Buchanan KL, Klein ME, Barth BB, Montoya MM, Shen X, Bohórquez DV. *Science* 2018;361(6408):eaat5236 | Full author list, title, journal, volume, issue, article number, date; glutamate, millisecond EPSPs, monosynaptic rabies tracing | Verified |
| 4 | Bellono NW, Bayrer JR, Leitch DB, et al. *Cell* 2017;170(1):185–98 | Title, first authors, journal, year; excitability, P/Q-type Ca²⁺ channels, 5-HT3 afferents, <1% of epithelium / >90% of body serotonin | `CONFIRM` full author list, pages |
| 5 | Bai L, Mesgarzadeh S, et al. *Cell* 2019;179(5):1129–43 | Title, first two authors, journal, year; target-specific single-cell sequencing; GLP1R⁺ IGLEs; Piezo2⁺ gastric stretch neurons | `CONFIRM` full author list, pages |
| 6 | Liu WW, Reicher N, Alway E, et al. (Bohórquez DV). *Nature* 2025;645(8081). doi:10.1038/s41586-025-09301-7 | Long author list, title, journal, volume, date, DOI; flagellin → TLR5 → PYY⁺ colonic neuropod cells → NPY2R vagal neurons → feeding; "neurobiotic sense" | Verified. **Load-bearing citation — check it personally** |
| 7 | Cryan JF, O'Riordan KJ, Cowan CSM, et al. *Physiol Rev* 2019;99(4):1877–2013 | Full author list, title, journal, volume, issue, pages, date | Verified |
| 8 | Kurilshikov A, Medina-Gomez C, Bacigalupe R, et al. *Nat Genet* 2021;53(2):156–65 | Title, joint first authors, journal, volume, pages, date; 18,340 individuals, 24 cohorts, 16S | Verified |
| 9 | Kim S, Kwon SH, Kam TI, et al. *Neuron* 2019;103(4):627–41 | Title, journal, year; gastric α-synuclein injection, transneuronal spread, truncal vagotomy and α-syn deficiency both protective | `CONFIRM` full author list, pages |
| 10 | Svensson E, Horváth-Puhó E, Thomsen RW, et al. *Ann Neurol* 2015;78(4):522–9 | Title, first author, journal, year; Danish registry, truncal vs superselective vagotomy 1975–1995, reduced PD risk after full truncal vagotomy | `CONFIRM` full author list, volume/pages |
| 11 | Neufeld KM, Kang N, Bienenstock J, Foster JA. *Neurogastroenterol Motil* 2011;23(3):255–64 | Title, authors, journal, year; reduced anxiety-like behaviour, central neurochemical change in germ-free mice | `CONFIRM` volume/pages |
| 12 | Vagal afferent fibre proportion (75–90%) | Figure confirmed across multiple reviews of vagal interoception | **No citation attached in the manuscript.** Attach a primary anatomical source or a named review before submission |
| 13 | Buck L, Axel R. *Cell* 1991;65(1):175–87 | Title, both authors, journal, year; multigene odorant receptor family; 2004 Nobel | `CONFIRM` volume/pages |

## Claims in the text with no citation attached

These were verified during writing but their bibliographic records were not captured. Each one
needs a reference before submission. Quoting a pooled effect size without its citation is the
exact failure the manuscript criticises in §3.5, so this list is not optional tidying.

1. **§3.4, the contradictory Mendelian randomisation studies.** Three separate results are
   described (5 positive / 6 negative; 10 protective / 10 deleterious; 15 positive / 16 negative
   with 36 reverse-direction). All three were located in search; none is cited. Either cite all
   three or rewrite the passage to describe the pattern without quoting specific counts.
2. **§3.5 and Table 1, every meta-analytic figure.** The probiotic pooled SMD −0.96 (95% CI
   −1.31 to −0.61, I² = 85%) and the ~⅓ fall after excluding high risk-of-bias studies; the
   −0.53 (95% CI −0.67 to −0.39) estimate; the FMT estimates of ≈−1.21, Hedges' g −0.81 and
   −0.10 (95% CI −0.60 to 0.41). **These are the manuscript's most load-bearing numbers and
   none carries a reference.** Attach them or remove them.
3. **§3.4, the 1×10⁻⁵ instrument threshold.** Standard practice in this literature and stated as
   such; needs a methodological citation or softening to "commonly relaxed thresholds".
4. **§7, the contemporaneous null vagotomy study.** A second Danish registry analysis finding no
   association is referred to and not cited.
5. **§4.4 / §1, the *Nature Reviews Gastroenterology & Hepatology* commentary** on the
   neurobiotic sense (doi:10.1038/s41575-025-01126-z) is useful context and currently unused.
6. **§3.2, vivarium-dependent microbiota variation as a source of irreproducibility.** Asserted
   from general knowledge of the gnotobiotic literature; needs a source.
7. **§8, enteric neuron count exceeding the spinal cord.** Widely repeated; cite it properly or
   drop the comparison.
8. **§6.3, NPY2R and 5-HT3 as established drug targets.** True and uncited.

## Reference list depth

Eleven cited sources is far short of what *Gut Microbes* reviews carry (typically 80–150).
That gap is a function of the verification constraint above, not of the argument's support: the
decision taken here was to cite only what had been checked rather than to pad the list to a
conventional length. Building it out is the main remaining task, and the claims above are where
to start.

## What was deliberately not done

- No citation was generated to support a sentence. Where no verified source existed, the claim
  is flagged above rather than dressed with a plausible-looking reference.
- No PRISMA diagram, no registration, no screening counts. This is a critical narrative review
  and says so in §2; the search strings and date carry an explicit placeholder for the authors
  to complete from a search they run themselves.
- No hidden characters. Checked for zero-width spaces, soft hyphens and Cyrillic or Greek
  homoglyphs: none present.
- No claim was made that the circuit account explains mood or cognition. §8 states the opposite,
  and the strongest objection to the paper's thesis is set out there in its own terms.
