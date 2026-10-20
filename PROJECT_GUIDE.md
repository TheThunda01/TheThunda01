# A quick guide to the projects

The common thread is making research decisions easier to inspect: what entered an analysis, what was calculated, and what the result can reasonably support. The projects cover different stages of that work. They are educational analyses and working software demonstrations, not claims of a new biological discovery.

## Pasilla expression QC

Gene-count tables are not ready-made biological answers. Library size, count composition, sample annotation, and transformation choices can affect exploratory views. This project uses public Drosophila counts to investigate those choices before asking a gene-level question.

It checks sample identifiers, summarizes counts, compares total-count and median-ratio normalization, and refits PCA after omitting each sample. Its value is the explicit sensitivity analysis: an influential sample becomes a question to investigate, not an automatic deletion. Key themes are **RNA-seq data structure, normalization, exploratory analysis, sample influence, and reproducibility**. It does not perform differential-expression testing or reproduce the original splicing study.

[Background and sources](https://github.com/TheThunda01/pasilla-expression-qc/blob/main/docs/project-context.md)

## Sequence Quality Toolkit

Sequence formats look simple, but malformed records, mismatched metadata, ambiguous symbols, and misunderstood quality scores can quietly undermine downstream work. This project makes a useful subset of those checks visible in a small command-line tool.

It streams FASTQ files, validates record structure, calculates per-read and per-cycle quality summaries, and checks FASTA records against sample manifests. A documented 1,000-read prefix from a public yeast RNA-seq run complements synthetic edge cases. Key themes are **file parsing, defensive programming, quality-score interpretation, provenance, and streaming computation**. The prefix cannot characterize the complete run, and quality scores are predictions rather than observed error measurements.

[Background and sources](https://github.com/TheThunda01/sequence-quality-toolkit/blob/main/docs/project-context.md)

## Surveillance data quality

A clean-looking surveillance curve can hide missing submissions, changing denominators, or revisions that arrived later. This project investigates what a summary is actually based on before interpreting its shape.

It audits a pinned CDC aggregate extract, checks counts and displayed percentages, compares snapshots, and uses synthetic report histories to reconstruct information available by a stated date. Key themes are **SQL, temporal data, missingness, denominators, revision handling, and provenance**. A complete extract is not proof of complete population coverage; one real snapshot cannot reveal historical reporting delays.

[Background and sources](https://github.com/TheThunda01/surveillance-data-quality/blob/main/docs/project-context.md)

## Cell-feature model validation

A classifier can achieve a strong benchmark score without establishing that it will help in a new setting. This project uses a public cell-image-feature dataset to examine evaluation choices rather than claim a clinical application.

It compares logistic regression, a small random forest, and a prior baseline using repeated nested cross-validation. It separates training-based threshold development from descriptive evaluation on a previously observed holdout and reports calibration and uncertainty with their scope. Key themes are **data leakage, model selection, calibration, decision thresholds, and honest evaluation**. The holdout is not newly blinded validation, and benchmark performance does not establish clinical utility.

[Background and sources](https://github.com/TheThunda01/cell-feature-model-validation/blob/main/docs/project-context.md)

## EvidenceTrail

Evidence-extraction tables need traceable records, consistent identifiers, and a clear way to inspect disagreements. Software can help with those mechanics while leaving scientific interpretation to a reviewer.

EvidenceTrail checks tables, compares reviewer records, shows how many submitted rows could be paired, and separates nonblank text agreement from missing entries. It records review decisions and exports the result. Key themes are **data schemas, evidence provenance, human review, missingness, and agreement denominators**. Matching text is not proof that an answer is correct or scientifically supported.

[Background and sources](https://github.com/TheThunda01/evidencetrail/blob/main/docs/project-context.md)

## Review Compass

A review plan is easier to discuss when its question, eligibility criteria, search ideas, and unresolved decisions are in one place. This project provides that planning structure and makes its automated cues deliberately modest.

It organizes a review plan, displays literal keyword matches for manual inspection, and exports planning notes. Field-completion counts describe what was entered; they do not score methodological quality. Key themes are **review planning, transparent automation, user-interface design, literal text matching, and human judgment**. Keyword cues cannot determine eligibility or understand negation and study design.

[Background and sources](https://github.com/TheThunda01/review-compass/blob/main/docs/project-context.md)

## Presenting the work on a résumé or CV

Put [github.com/TheThunda01](https://github.com/TheThunda01) in the contact header. For a role with a particular focus, link one or two relevant repositories beside the project entries so the reader does not have to search. Use claims you can explain and demonstrate yourself.

Example wording, after reviewing and reproducing the work:

> **Computational biology and research software portfolio** — Developed and documented Python, SQL, and JavaScript projects covering RNA-seq quality exploration, sequence-file validation, surveillance data auditing, model evaluation, and evidence-review workflows. Included reproducible examples, automated checks, source attribution, and explicit methodological limitations.

On a detailed CV, list these under Projects or Research Software. Keep them separate from peer-reviewed publications. AI assistance and the distinction between implemented features and future plans are disclosed in the repositories.
