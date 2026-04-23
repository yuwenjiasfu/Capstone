## Report

The full report is available here:

[**A Empirical Study of 15 Android BLE Health Applications: Comprehensive Findings Report**](./final_report.pdf)


# Capstone Repository: Android Health / BLE App Security and Privacy Analysis

## Overview

This repository is the working space for a capstone project on security and privacy analysis of Android health, fitness, and BLE-related applications.

It is not only a collection of final conclusions. It also preserves the intermediate materials that led to those conclusions, including:

- original APK / XAPK packages;
- decompiled app archives;
- rule databases organized from papers;
- automated keyword / rule search results;
- per-app evidence chains, summary notes, and independent findings.

In other words, this repository is closer to a research workspace than to a fully polished product repository. It keeps raw inputs, intermediate artifacts, manual notes, and stage-by-stage summaries together.

Chinese version: `README_CN.md`

## Repository Snapshot

As of April 22, 2026, this repository contains:

- 19 original APK / XAPK packages in the repository root;
- 15 analyzed app folders under `app/`;
- 15 corresponding search-result folders under `search/`;
- 15 decompiled archives under `app/<app-name>/`;
- 2 literature databases under `database/`;
- about 1.65 GB of total data.

This is also why the project was ultimately uploaded to GitHub instead of being sent by email.

## Analyzed App Folders

The current folders under `app/` are:

`blehealth+`, `bruhealth`, `bupa`, `fitpro`, `healthcare`, `lightblue`, `myvitale`, `nRF`, `nutrack`, `polarbeat`, `rossmax`, `weighttrack`, `xdrip`, `xiangshan`, `yuwell`

The repository root also keeps the original package files. However, those original filenames do not always map one-to-one to the normalized folder names under `app/`. Some filenames are in English, some are in Chinese, and some have aliases or duplicate naming. So the package names in the root cannot always be matched directly to the folder names under `app/`.

## Meaning of the Main Folders

### 1. Repository root

The repository root stores the original APK / XAPK packages, which are the raw inputs of the whole analysis process.

As a result, the root looks crowded:

- it contains large binary packages;
- it also contains the main `README.md`;
- and it sits directly alongside `app/`, `database/`, `search/`, and `tools/`.

### 2. `app/`

This folder stores the analysis materials for each app.

At the moment, each app folder generally has the same high-level structure:

- one decompiled archive (`*.zip`);
- one `finding.txt`;
- one `evidence/summary_notes.txt`;
- one `evidence/evidence_notes.txt`.

An important detail is that the decompiled content is usually kept as a ZIP archive, rather than committed as a fully extracted directory tree. Common paths inside those archives include:

- `resources/AndroidManifest.xml`
- `resources/assets/...`
- `sources/...`

For some APK / XAPK / split-package samples, the internal archive structure can also differ. For example, some archives may use paths like `resources/<package-name>.apk/...` instead of a single flat `resources/...` layout.

So when a note references `resources/AndroidManifest.xml` or `sources/...`, that path often refers to a path inside the ZIP archive rather than to an already-extracted directory committed in the repository.

### 3. `database/`

This folder contains two literature databases used at different stages of the project.

#### `database/database_original/`

This is the earlier and broader paper database built in the project.

It contains:

- `paper_catalog.tsv`: paper index;
- `snapshots/`: local HTML snapshots;
- `papers/`: local PDFs when available.

This database is broader and less constrained, and is more suitable for background understanding, manual reading, and independent reasoning.

The paper IDs here use the `Pxxx` form, such as `P001`, `P013`, and `P023`.

#### `database/database_main/`

This is the later and more structured rule database, used to support the later rule-based analysis workflow.

It contains:

- `rule_catalog.txt`: the structured rules used in the later stage;
- `README.md`: database description;
- `snapshots/`: local HTML source snapshots;
- `papers/`: local PDF papers.

This database is more operational and more suitable for reuse during app-by-app review.

The source paper IDs here use the `Bxxx` form. In the later automated search workflow, `BRxxx` also appears, which is the rule ID format.

### 4. `search/`

This folder stores the automated rule-search results for each app.

Each app folder usually contains:

- `rule_hits.tsv`: raw hits in table form;
- `rule_hits.md`: a more readable version of the hits;
- `no_hit_rules.txt`: the list of rules that did not hit in that app.

These files are candidate evidence, not final conclusions.

Their main purpose is to:

- narrow the range of manual follow-up;
- show which rules hit related content in the app;
- support later manual review.

Search hits alone are not enough to prove that a security or privacy issue has been confirmed.

### 5. `tools/`

This folder stores the Python scripts used for keyword / rule search.

The main script is:

- `tools/rule_code_search.py`

It performs rule-based static searching over decompiled content and writes the results to `search/<app-name>/`.

There is also a `rule_search_outputs/` directory under `tools/`. It is just an example of output produced by the Python file and can be ignored.

## Overall Workflow

The rough workflow of the project is:

1. Collect the original APK / XAPK packages.
2. Decompile or unpack the apps, and store the results as ZIP archives under `app/<app-name>/`.
3. Use the paper databases to decide what kinds of security and privacy issues are worth checking.
4. Produce my own findings based on my own knowledge and my understanding of the papers in `database_original`.
5. Run the Python rule-search script to search code, resources, configuration, and paths for keywords, API clues, and possible evidence locations.
6. Manually review the search results.
7. Build the evidence chains.
8. Write the summary for each app.

The most important point is that this repository reflects a mixed workflow of automated filtering plus manual reasoning. The automation only narrows the scope. Final judgment still depends heavily on manual reading and understanding.

## Meaning of Each File Type

### `search/<app-name>/rule_hits.tsv` and `rule_hits.md`

These two file types are automated search outputs.

They tell you:

- which rules hit;
- where the hits are;
- which paper or rule source each hit came from.

They do **not** mean that an issue has already been confirmed.

### `app/<app-name>/evidence/summary_notes.txt`

This is the more structured summary, mainly corresponding to the later `database_main/` workflow.

These `summary_notes.txt` files usually come from:

- the more structured rules in `database_main/`;
- the Python search script;
- manual follow-up on the hits;
- manually constructed evidence chains.

So this part is closer to conclusions that have paper sources and a relatively more complete evidence chain.

### `app/<app-name>/evidence/evidence_notes.txt`

This is the more detailed evidence-chain note and reasoning note.

It usually records:

- which files are most important;
- how a code path or evidence chain was connected step by step;
- why certain rules are treated as `confirmed`, `supported_hypothesis`, or `not_testable`;
- what boundaries and limitations the current evidence still has.

### `app/<app-name>/finding.txt`

This file is different from `summary_notes.txt`.

`finding.txt` depends more on:

- the earlier `database_original/`;
- paper conclusions that are hard to quantify;
- ideas that are hard to summarize as code-search rules;
- my own manual judgment based on my understanding of security and privacy.

So `finding.txt` is better understood as independent manual analysis, rather than a fully rule-based and fully repeatable output.

## Important Reading Notes

The following boundaries are important when reading this repository.

### 1. `summary_notes.txt` is not exhaustive

`summary_notes.txt` is mainly based on the later rule system in `database_main/`, together with my own Python keyword / rule filtering code.

After the script filters once, I manually follow the more promising locations and connect the evidence chain.

However, in many places my search code is intentionally narrow. The reason is practical: the code volume is too large, and if the number of hits becomes too high, I cannot manually trace all of them.

That leads to several consequences:

- some relevant risks may really exist but may not appear in `summary_notes.txt`;
- some relevant code paths may have been missed because the search patterns were too narrow;
- some rules are suitable for first-pass screening, but their recall may still be limited.

So `summary_notes.txt` is better understood as the part of the results that I found, followed, and organized into evidence chains with relatively stronger support, rather than proof that all important issues have already been covered.

### 2. `finding.txt` is more subjective

`finding.txt` relies more on `database_original/`, on papers that are difficult to convert directly into rules, and on my own understanding of security and privacy.

That means:

- some findings are hard to quantify;
- some findings are hard to convert into keyword-search patterns;
- some judgments depend on interpretation and understanding;
- some conclusions may be incomplete, and some may also be not entirely correct.

So `finding.txt` is manual analysis, but it should not be treated as perfectly accurate ground truth.

### 3. Search hits do not equal confirmed vulnerabilities

The results in `search/` are only candidate evidence locations.

A single hit may only mean:

- a rule found a related keyword;
- a file path is worth further tracing;
- a piece of code looks like it needs manual review.

A hit does **not** automatically mean that a complete security or privacy issue has been proven.

## GitHub Upload / Redaction Note

Some app packages or decompiled contents contained plaintext content that I considered security-sensitive, such as API keys or other sensitive strings.

Because GitHub has restrictions around this kind of plaintext content, the original form could not always be uploaded directly. So before committing the repository, I modified, replaced, or sanitized some of that content.

This leads to several consequences:

- some summary wording is more general than in my original local notes;
- some findings and conclusions cannot be written in very specific terms;
- some real sensitive plaintext values do not appear directly in the GitHub-visible version.

If you need to see the original problematic plaintext, the suggested approach is:

1. first unzip the corresponding archive under `app/<app-name>/`;
2. then keep following the paths given in the evidence chain;
3. inspect the original content locally at the referenced location.

In other words, this repository tries to preserve the evidence path, but it does not preserve every sensitive plaintext value in a form that can be directly viewed on GitHub.

## Current Limitations and Known Problems

This project currently has several important limitations.

### 1. Coverage is incomplete

The biggest practical limitation is search coverage.

Because the code volume is large, once the raw hit count becomes too high it exceeds what can realistically be followed manually. So the Python filtering logic has to stay relatively narrow in many places. That improves practicality, but it also increases the chance of misses.

### 2. Some risks may still exist even if they were not found

It is entirely possible that a relevant risk exists but was not surfaced by the current workflow.

Common reasons include:

- the keyword list was too narrow;
- the app used a non-obvious implementation;
- the relevant code path appeared in an unexpected namespace or file type;
- the issue depended more on runtime behavior, which is hard to discover through static search.

### 3. Manual review capacity is itself a bottleneck

Even after filtering, the number of hits can still be large. Continuing to trace them manually is time-consuming, so in practice it is impossible to dig infinitely deep for every app and every rule.

### 4. Some papers are inherently hard to operationalize

Many valuable papers cannot be translated naturally into rigid, directly checkable app rules.

That is also why the project ended up with two databases:

- a broader, more interpretive `database_original/`;
- a narrower, more operational `database_main/`.

This split is helpful, but it also means the repository actually contains two kinds of evidence with two different confidence models.

### 5. Reproducibility is still not good enough

This repository preserves the workflow, but it has not reached the point where the whole process can be fully reproduced with a single clean command.

For example:

- the decompiled results are stored as ZIP archives, not as a fully scripted unpacking pipeline;
- the search script still contains hard-coded absolute paths;
- reproducing the workflow cleanly on another machine would still require more path cleanup and workflow cleanup.

### 6. Naming and directory structure are more like practical work products than elegant design

This repository prioritizes preserving evidence, not building a repository with perfectly unified naming and perfectly clean directory structure.

So some usability issues remain:

- raw APK / XAPK packages are placed directly in the root;
- the per-app analysis directory is called `app/`, but the repository itself is also a working space, which can be confusing;
- some original package names have duplicates, aliases, or mixed Chinese / English naming;
- internal archive structures can differ across apps because of APK / XAPK / split packaging;
- some file or folder names may still not fully match the naming scheme I tried to standardize later.

There is also a historical reason behind this. At the beginning of the project, the structure, naming system, and full workflow were not yet fully designed. A lot of the analysis and writing was developed step by step. When some data, files, and folders were first created, I had not yet fully decided whether they would become part of the formal workflow, so some names and paths were changed many times during the process.

Later, I did spend a lot of time trying to make these materials more consistent. But because the project involves more than a dozen apps and dozens of rules per app, it is hard to avoid some leftover old names, old paths, or inconsistent references.

If you find that a file mentioned in a note cannot be found at the stated location, this is probably the reason. In that case, please tell me and I can manually trace what file it was originally meant to point to.
