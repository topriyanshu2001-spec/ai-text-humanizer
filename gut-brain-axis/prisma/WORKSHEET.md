# Fifteen-minute worksheet

Ten numbers. Work down the page, write each number in the blank, then copy them into
`counts_minimal.json` and run the renderer. Nothing here needs a subscription except Embase
and Web of Science — skip those and set them to 0 if you have no access, and say so in the
Methods.

---

## Step 1 — four searches (about 8 minutes)

Run each query, read the result count off the screen, write it down.

### 1a. PubMed/MEDLINE — free, no login

Go to **pubmed.ncbi.nlm.nih.gov**, paste this whole block into the search box, press Enter.
The count appears as "N results" just above the first record.

```
(("Gastrointestinal Microbiome"[Mesh] OR microbiot*[tiab] OR microbiome[tiab]) AND ("Brain-Gut Axis"[Mesh] OR "gut-brain"[tiab] OR "brain-gut"[tiab] OR depress*[tiab] OR anxiet*[tiab] OR behaviour*[tiab] OR behavior*[tiab])) AND (("Enteroendocrine Cells"[Mesh] OR "Enterochromaffin Cells"[Mesh] OR neuropod*[tiab] OR "Vagus Nerve"[Mesh] OR "Nodose Ganglion"[Mesh] OR "vagal afferent*"[tiab] OR vagotomy[tiab] OR "Optogenetics"[Mesh]) OR ("Fecal Microbiota Transplantation"[Mesh] OR "Probiotics"[Mesh] OR probiotic*[tiab] OR psychobiotic*[tiab] OR "germ-free"[tiab] OR gnotobiot*[tiab] OR "mendelian randomi*"[tiab]))
```

**PubMed/MEDLINE count: ______________**

### 1b. Scopus — institutional login

**scopus.com** → Advanced search → paste:

```
TITLE-ABS-KEY(microbiot* OR microbiome) AND TITLE-ABS-KEY("gut-brain" OR "brain-gut" OR depress* OR anxiet* OR behaviour* OR behavior*) AND TITLE-ABS-KEY(neuropod* OR enteroendocrine OR enterochromaffin OR "vagal afferent*" OR nodose OR vagotomy OR optogenetic* OR probiotic* OR psychobiotic* OR "microbiota transplant*" OR "germ-free" OR gnotobiot* OR "mendelian randomi*")
```

**Scopus count: ______________**

### 1c. Embase — institutional login, or write 0 and say so

**embase.com** → Search → Advanced:

```
('intestine flora'/exp OR microbiot*:ti,ab OR microbiome:ti,ab) AND ('brain gut axis'/exp OR 'gut-brain':ti,ab OR depress*:ti,ab OR anxiet*:ti,ab) AND ('enteroendocrine cell'/exp OR 'enterochromaffin cell'/exp OR neuropod*:ti,ab OR 'vagus nerve'/exp OR vagotomy:ti,ab OR 'feces transplantation'/exp OR probiotic*:ti,ab OR 'germ free':ti,ab OR 'mendelian randomi*':ti,ab)
```

**Embase count: ______________**

### 1d. Web of Science — institutional login, or write 0 and say so

**webofscience.com** → Advanced Search:

```
TS=(microbiot* OR microbiome) AND TS=("gut-brain" OR "brain-gut" OR depress* OR anxiet* OR behaviour* OR behavior*) AND TS=(neuropod* OR enteroendocrine OR enterochromaffin OR "vagal afferent*" OR nodose OR vagotomy OR optogenetic* OR probiotic* OR psychobiotic* OR "microbiota transplant*" OR "germ-free" OR gnotobiot* OR "mendelian randomi*")
```

**Web of Science count: ______________**

---

## Step 2 — deduplicate (about 3 minutes)

Export all four result sets to RIS or BibTeX, import into **Zotero**, **EndNote** or **Rayyan**,
and run duplicate detection.

**Duplicates removed: ______________**

Your deduplication tool: ______________

---

## Step 3 — screen titles and abstracts (this is the real work)

Screen the deduplicated set. For a review of this scope you are looking for anything that
reports a gut-to-brain signalling mechanism, a microbiome–brain association, or an intervention
with a neural or behavioural outcome.

**Records excluded at title/abstract: ______________**

Of those left, how many full texts could you not obtain?

**Reports not retrieved: ______________**

---

## Step 4 — full-text exclusions, with reasons

Read the remaining full texts. Log each exclusion with its reason in
`screening_log_template.csv`. The three reasons below cover most of what you will drop; rename
them in the JSON if yours differ.

**Not a gut-brain signalling study: ______________**

**No primary data (commentary, editorial, conference abstract): ______________**

**No neural or behavioural outcome: ______________**

---

## Step 5 — citation searching

Scan the reference lists of the reviews you retrieved. How many *new* records did that surface,
that the databases had missed?

**New records from citation searching: ______________**

How many of those turned out to be duplicates of database records?

**Duplicates of database records: ______________**

Set both to 0 if you did not do citation searching; the figure drops that arm automatically.

---

## Step 6 — the included set

**Reports of included studies: ______________**

This is usually the same as the number of studies, and larger when one study produced several
papers. The script derives the number of *studies* itself and will tell you if the two conflict.

---

## Step 7 — render

Copy your numbers into `counts_minimal.json`, then:

```bash
pip install matplotlib pillow
cd gut-brain-axis/prisma
python3 make_prisma.py --counts counts_minimal.json
```

If anything does not reconcile the script says which equation failed and refuses to draw. Fix
the number it names and run again. Output lands in `out/` as PDF, SVG, EPS, 600 dpi PNG and
TIFF.

---

## If you would rather not do this at all

You do not have to. The manuscript's Methods section now reports the search in prose, which is
the convention your own migraine review follows and which is accepted practice for a critical
narrative review. The figure is polish, not a requirement — a narrative review is not expected
to carry a PRISMA flow diagram, and carrying one without a protocol registration invites
questions you would rather not field.

Fill in the search date and the databases you actually used in Section 2, and the manuscript is
complete without this figure.
