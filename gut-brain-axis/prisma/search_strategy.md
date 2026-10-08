# Search strategy — gut–brain axis review

Fully specified, reproducible search strings for each database. Run these as written, record
the hit count each returns, and enter the counts in `counts.json`.

**Nothing in this file is a result.** These are queries. The numbers come from running them.

---

## Concept blocks

The search is built from four blocks, combined as `(B1 AND B2) AND (B3 OR B4)`.

| Block | Concept |
|---|---|
| **B1** | Gut microbiota / microbiome |
| **B2** | Gut–brain communication and central outcomes |
| **B3** | Neuroepithelial and vagal transduction (the circuit arm) |
| **B4** | Compositional evidence and intervention designs (the compositional arm) |

Running both arms matters. A search limited to B3 recovers the circuit literature and misses the
compositional literature the review criticises; a search limited to B4 does the reverse. The
review's argument depends on having both in view.

---

## 1. PubMed / MEDLINE

Interface: https://pubmed.ncbi.nlm.nih.gov — paste as a single line into the search box, then
read the result count from "N results".

```
(
  ("Gastrointestinal Microbiome"[Mesh] OR microbiot*[tiab] OR microbiome[tiab]
   OR "gut flora"[tiab] OR "intestinal bacteria"[tiab] OR "commensal bacteria"[tiab])
)
AND
(
  ("Brain-Gut Axis"[Mesh] OR "gut-brain"[tiab] OR "brain-gut"[tiab]
   OR "gut brain axis"[tiab] OR "microbiota-gut-brain"[tiab]
   OR "Depressive Disorder, Major"[Mesh] OR depress*[tiab] OR anxiet*[tiab]
   OR "Behavior, Animal"[Mesh] OR behaviour*[tiab] OR behavior*[tiab]
   OR "Parkinson Disease"[Mesh] OR "Autism Spectrum Disorder"[Mesh])
)
AND
(
  ("Enteroendocrine Cells"[Mesh] OR "Enterochromaffin Cells"[Mesh]
   OR neuropod*[tiab] OR "enteroendocrine"[tiab] OR "enterochromaffin"[tiab]
   OR "Vagus Nerve"[Mesh] OR "Nodose Ganglion"[Mesh]
   OR "vagal afferent*"[tiab] OR "nodose"[tiab] OR "vagotomy"[tiab]
   OR "Toll-Like Receptor 5"[Mesh] OR "Synaptic Transmission"[Mesh]
   OR "sensory transduction"[tiab] OR "labelled line*"[tiab] OR "labeled line*"[tiab]
   OR "Optogenetics"[Mesh] OR "Interoception"[Mesh])
  OR
  ("Fecal Microbiota Transplantation"[Mesh] OR "Probiotics"[Mesh]
   OR probiotic*[tiab] OR psychobiotic*[tiab] OR "faecal microbiota transplant*"[tiab]
   OR "fecal microbiota transplant*"[tiab] OR "germ-free"[tiab] OR gnotobiot*[tiab]
   OR "Mendelian Randomization Analysis"[Mesh] OR "mendelian randomi*"[tiab]
   OR "16S"[tiab] OR metagenom*[tiab] OR "short-chain fatty acid*"[tiab])
)
```

**Limits:** none on language or date at the search stage. Apply restrictions at screening and
record them as exclusion reasons, so the flow diagram shows what they removed.

**Record:** the result count → `counts.json` → `databases.pubmed`

---

## 2. Embase

Interface: Embase.com (Elsevier). Emtree terms differ from MeSH; `/exp` explodes the tree.

```
('intestine flora'/exp OR microbiot*:ti,ab OR microbiome:ti,ab OR 'gut flora':ti,ab)
AND
('brain gut axis'/exp OR 'gut-brain':ti,ab OR 'brain-gut':ti,ab
 OR 'major depression'/exp OR depress*:ti,ab OR anxiet*:ti,ab
 OR 'animal behavior'/exp OR 'Parkinson disease'/exp OR 'autism'/exp)
AND
(('enteroendocrine cell'/exp OR 'enterochromaffin cell'/exp OR neuropod*:ti,ab
  OR 'vagus nerve'/exp OR 'nodose ganglion'/exp OR 'vagal afferent*':ti,ab
  OR vagotomy:ti,ab OR 'toll like receptor 5'/exp OR 'optogenetics'/exp
  OR 'sensory transduction':ti,ab OR interoception:ti,ab)
 OR
 ('feces transplantation'/exp OR 'probiotic agent'/exp OR probiotic*:ti,ab
  OR psychobiotic*:ti,ab OR 'germ free':ti,ab OR gnotobiot*:ti,ab
  OR 'mendelian randomi*':ti,ab OR '16S':ti,ab OR metagenom*:ti,ab
  OR 'short chain fatty acid'/exp))
```

**Record:** → `counts.json` → `databases.embase`

---

## 3. Scopus

Interface: scopus.com → Advanced search.

```
TITLE-ABS-KEY ( microbiot* OR microbiome OR "gut flora" )
AND TITLE-ABS-KEY ( "gut-brain" OR "brain-gut" OR "gut brain axis"
                    OR depress* OR anxiet* OR behaviour* OR behavior*
                    OR parkinson* OR autism* )
AND TITLE-ABS-KEY ( neuropod* OR enteroendocrine OR enterochromaffin
                    OR "vagal afferent*" OR nodose OR vagotomy
                    OR "toll-like receptor 5" OR optogenetic*
                    OR "sensory transduction" OR interoception
                    OR probiotic* OR psychobiotic* OR "microbiota transplant*"
                    OR "germ-free" OR gnotobiot* OR "mendelian randomi*"
                    OR "16S" OR metagenom* OR "short-chain fatty acid*" )
```

**Record:** → `counts.json` → `databases.scopus`

---

## 4. Web of Science Core Collection

Interface: webofscience.com → Advanced Search. `TS=` searches topic (title, abstract, keywords).

```
TS=(microbiot* OR microbiome OR "gut flora")
AND TS=("gut-brain" OR "brain-gut" OR "gut brain axis" OR depress* OR anxiet*
        OR behaviour* OR behavior* OR parkinson* OR autism*)
AND TS=(neuropod* OR enteroendocrine OR enterochromaffin OR "vagal afferent*"
        OR nodose OR vagotomy OR "toll-like receptor 5" OR optogenetic*
        OR "sensory transduction" OR interoception OR probiotic* OR psychobiotic*
        OR "microbiota transplant*" OR "germ-free" OR gnotobiot*
        OR "mendelian randomi*" OR "16S" OR metagenom* OR "short-chain fatty acid*")
```

**Record:** → `counts.json` → `databases.web_of_science`

---

## 5. PsycINFO (APA PsycNET or Ovid)

Relevant because the compositional literature is heavily psychiatric and PsycINFO indexes
journals the biomedical databases miss.

```
(microbiot* OR microbiome OR "gut flora").ti,ab.
AND ("gut-brain" OR "brain-gut" OR depress* OR anxiet* OR behavio*).ti,ab.
AND (probiotic* OR psychobiotic* OR "microbiota transplant*" OR "germ-free"
     OR vagal OR vagus OR enteroendocrine OR neuropod*).ti,ab.
```

**Record:** → `counts.json` → `databases.psycinfo`

---

## 6. Cochrane CENTRAL

For the intervention arm — probiotic and faecal transplantation trials.

```
#1  MeSH descriptor: [Gastrointestinal Microbiome] explode all trees
#2  (microbiot* OR microbiome OR probiotic* OR psychobiotic*):ti,ab,kw
#3  MeSH descriptor: [Fecal Microbiota Transplantation] explode all trees
#4  (depress* OR anxiet* OR mood OR cognit*):ti,ab,kw
#5  (#1 OR #2 OR #3) AND #4
```

**Record:** → `counts.json` → `databases.cochrane_central`

---

## 7. Registers

- **ClinicalTrials.gov** — condition: depression OR anxiety; intervention: probiotic OR
  "fecal microbiota transplantation"
- **PROSPERO** — to identify existing or in-progress reviews on this question (also a
  duplication check before you commit)

**Record:** → `counts.json` → `registers.*`

---

## 8. Other methods (the right-hand arm of the diagram)

PRISMA 2020 separates records found outside database searching. Record each separately:

- **Citation searching** — backward (reference lists of included reports) and forward (works
  citing them). Record how many *new* records this surfaced.
- **Websites / organisations** — e.g. PRISMA statement site, WHO, regulatory documents.
- **Hand-searching** — specific journals scanned directly, if any.

**Record:** → `counts.json` → `other_methods.*`

---

## Recording discipline

Three rules, and they are what makes the diagram defensible:

1. **Record the count the moment you run the query**, along with the date. Database contents
   change; a count from last month will not reproduce.
2. **Export the records**, do not just note the number. Deduplication and screening both need
   the actual records, and a reviewer may ask for the export.
3. **Log every exclusion with its reason** at full-text stage, in
   `screening_log_template.csv`. The flow diagram's "Reports excluded" box needs reasons with
   counts, and those counts must sum to the total excluded.

## Search date

Record the date each search was executed. If searches run on different dates, record the
latest, and state in the Methods section that the search was last updated on that date.

> The Methods section of `MANUSCRIPT.md` carries a `[TO CONFIRM BEFORE SUBMISSION]` block for
> exactly these fields. Fill it from what you actually run.
