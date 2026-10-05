# Verification log

Every reference in `MANUSCRIPT.md` was checked against the published record before it entered
the text. Nothing was written from memory and nothing was inferred from a plausible-looking
pattern. This file records what was confirmed, what was not, and what the authors must still
close out before submission.

## Why this file exists

The manuscript argues that an unverifiable exposure record makes a literature uninterpretable.
A reference list assembled the same way would make the manuscript uninterpretable. The two
failures are the same failure, so the standard applied here is the one the paper asks of others.

## Environment constraint affecting verification

This work ran in a container whose network policy denied `pubmed.ncbi.nlm.nih.gov`,
`pmc.ncbi.nlm.nih.gov`, `sciencedirect.com`, `api.crossref.org`, `doi.org`,
`api.semanticscholar.org` and `europepmc.org` (403 at the proxy on CONNECT). Verification
therefore ran through web search rather than direct database or DOI resolution.

Consequence: **titles, journals, years and principal findings are confirmed; full author
strings, volume/page ranges and DOIs are confirmed only where a search result displayed them.**
Fields marked `CONFIRM` below need a one-minute check against the journal's own page. That is
a real limitation of this draft, not a formality.

To remove the constraint for future work, add those hosts under Allowed domains in the
environment's Network access settings, or widen the access level.

## The retraction catch

The most-cited evidence in this field is the 2013 *BMC Medicine* DNA barcoding study reporting
that 59% of North American herbal products contained undisclosed substitutions.

**It was retracted in July 2024.** A University of Guelph investigation found evidence of data
fabrication; four authors disagree with the retraction.

That figure appears in reviews published well after the retraction. It was kept out of this
manuscript's evidence base and is cited only as reference [6], explicitly as a retraction, to
make the point about provenance. Replacement evidence came from Seethapathy et al. [9], Ichim
[10] and Vassou et al. [11], none of which carries a retraction or expression of concern as far
as searching showed.

**Check before submission:** re-run a retraction search on all 18 references. Retraction Watch
and the Crossref `update-to` field are the quickest routes. This is cheap and it is the single
highest-value check on the list.

## Reference status

| # | Source | Verified | Status |
|---|---|---|---|
| 1 | Navarro VJ, et al. HDS liver injury, DILIN. *Hepatology* 2014;60(4):1399–408 | Title, journal, year, finding (7%→20%; 45 bodybuilding / 85 non-bodybuilding / 709 medications; worse outcomes for non-bodybuilding HDS) | Author string truncated at "et al." — `CONFIRM` full list, volume/pages |
| 2 | Teschke R, Danan G. Worldwide RUCAM use, 81,856 DILI + 14,029 HILI cases | Title, both authors, finding, and the authentication/batch-variability limitation quoted in §1 and §4.4 | `CONFIRM` journal (*Medicines* (Basel) 2020;7(10):62), volume/pages |
| 3 | Danan G, Teschke R. RUCAM update. *Int J Mol Sci* 2016;17(1):14 | Title, authors, journal, year, R-value and injury-pattern structure | `CONFIRM` page/article number |
| 4 | Nagral A, Adhyaru K, Rudra OS, Gharat A, Bhandare S. *J Clin Exp Hepatol* 2021;11(6):732–8 | Full author list, title, journal, year, volume, pages | Verified |
| 5 | Kulkarni AV, Hanchanale P, Prakash V, Kalal C, Sharma M, Kumar K, et al. *Hepatol Commun* 2022;6(6):1289–300 | First six authors, title, journal, volume, issue, pages; 13 centres / 9 locations / 43 patients / 46-day median / 67.4% probable / ANA commonest | Verified. One search result expanded "Kulkarni AV" to a full given name — that expansion was **not** trusted and initials are used |
| 6 | Retraction Note, DNA barcoding. *BMC Med* 2024 | Retraction confirmed, July 2024, Guelph investigation, fabrication finding | `CONFIRM` retraction note volume/article number |
| 7 | Vanherweghem JL, et al. *Lancet* 1993;341(8842):387–91 | Title, first author, journal, year, the *Aristolochia fangchi* / *Stephania tetrandra* substitution, >100 Belgian cases | `CONFIRM` full author list, pages |
| 8 | Nortier JL, et al. *N Engl J Med* 2000;342(23):1686–92 | Title, first author, journal, year, urothelial carcinoma finding | `CONFIRM` full author list, pages |
| 9 | Seethapathy GS, Raclariu-Manolica AC, Anmarkrud JA, Wangensteen H, de Boer HJ. *Front Plant Sci* 2019;10:68 | Full author list, title, journal, volume, article number, DOI 10.3389/fpls.2019.00068; 79 products, 67%/21%/24% fidelity, 8 of 27 | Verified |
| 10 | Ichim MC. *Front Pharmacol* 2019;10:1227 | Sole author, title, journal, volume, article, date; 5,957 products / 37 countries / 27%; continental breakdown | Verified |
| 11 | Vassou SL, Nithaniyal S, Raju B, Parani M. *Diversity* 2022;14(6):495 | Title, journal, volume, issue, article; 46% adulterant via rbcL | `CONFIRM` author list |
| 12 | Saper RB, Phillips RS, Sehgal A, Khouri N, Davis RB, Paquin J, et al. *JAMA* 2008;300(8):915–23 | Author list, title, journal, year; 193 products / 37 manufacturers / 25 sites / 20.7% / rasa shastra >2× | Verified. Also cited as ref 60 in the migraine manuscript in this repo |
| 13 | Nagral A, et al. HILI guide to approach, *Tinospora* lessons. *J Clin Exp Hepatol* 2023;13(2) | Title, first author, journal, Mar–Apr 2023; **4 raw plant samples + 2 commercial preparations; 4/4 identified; 0/2 analysable** | `CONFIRM` full author list and page range. **This is the load-bearing citation of the paper — verify it personally** |
| 14 | Góis et al. Irregular herbal products, chemical authentication + updated RUCAM. *Case Rep Hepatol* 2026 | Title, journal, DOI 10.1155/crhe/5905774 | Author initials **not** confirmed — placeholder in the text. `CONFIRM` before submission |
| 15 | Heinrich M, et al. ConPhyMP guidelines. *Front Pharmacol* 2022;13:953205 | Title, journal, article number, adoption as peer-review element | `CONFIRM` full author list |
| 16 | *Journal of Ethnopharmacology* Guide for Authors | Voucher specimen requirement, World Flora Online botanical names with authorities, 250-word structured abstract | Access blocked by network policy; confirmed via secondary sources. `CONFIRM` directly and date the access |
| 17 | Philips CA, Theruvath AH. *Medicine* (Baltimore) 2024;103(16):e37903 | Both authors, title, journal, volume, issue, article, date | Verified. Cited for positioning, not for a factual claim |
| 18 | LiverTox: Tinospora. NCBI Bookshelf NBK608429 | Record exists | `CONFIRM` accession and access date |

## Claims in the text that still need a citation

These statements are correct but currently carry no reference. They need one before submission,
or they need softening to match what is actually cited.

1. **§3.3** — DILIN expert-opinion adjudication and the structured-vs-holistic comparison
   literature. Written from general knowledge of the method. Needs the DILIN methodology paper.
2. **§4.3** — undeclared synthetic adulterants (glucocorticoids, NSAIDs) in traditional
   joint-pain products. Asserted without a source. Either cite a documented series or cut it.
3. **§4.4** — chemotype, harvest-season and plant-stress variation in secondary metabolites.
   The RUCAM limitation is cited to [2]; the phytochemical variability claim is not.
4. **§4.2 (added paragraph)** — the three interaction mechanisms (shared metabolic route,
   CYP450 induction/inhibition, protein-binding displacement). Standard pharmacology, but a
   review should cite it.
5. **§8** — India's pharmacovigilance programme for ASU drugs, and WHO traditional medicine
   safety guidance. Both named, neither cited.
6. **§5** — the Ministry of AYUSH statement. A PIB press release from July 2021 exists
   (PRID 1733260); `CONFIRM` and cite properly, or attribute more loosely.
7. **§4.1** — *T. crispa* / *T. cordifolia* morphological similarity, interchangeable trade and
   differing clerodane furanoditerpenoid content. Needs a phytochemistry source.

## Methods section

`MANUSCRIPT.md` §2 carries a `[TO CONFIRM BEFORE SUBMISSION]` block. The databases, search
strings and final search date must be filled in from a search the authors actually execute.
They are not asserted in the draft, deliberately — an invented methods statement would be the
same category of error the paper is about.

## What was deliberately not done

- No citation was generated to support a sentence. Where no verified source existed, the claim
  is flagged above rather than dressed with a plausible reference.
- No DOI was constructed. Where a DOI was not displayed in a verified result, none is printed.
- No author name was expanded from initials, even where a search result offered an expansion.
- No PRISMA flow diagram, no PROSPERO registration, no screening counts. This is a critical
  narrative review and says so; fabricating screening numbers for an unrun search would be
  research misconduct, not formatting.
- No hidden characters. The file was checked for zero-width spaces, soft hyphens and Cyrillic
  or Greek homoglyphs: none present.
