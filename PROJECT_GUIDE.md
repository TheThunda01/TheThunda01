# A quick guide to the projects

The ten projects connect two kinds of work: building models of molecular measurements, and making the data and research decisions behind those models easier to inspect. The collection reflects my interests in computational biology, AI, mathematical modeling, and experimental molecular biology. It is a foundation for future research, not a claim that I have conducted new laboratory experiments or established new mechanisms.

The molecular projects ask how model assumptions, structural evidence, selection budgets, and chemical similarity affect an answer. The six foundation projects support that work through data quality, statistical evaluation, reproducibility, and evidence review. Together they move from a biological question to an inspectable analysis without treating a prediction as an experimental result.

**For a résumé or CV: [github.com/TheThunda01](https://github.com/TheThunda01).**

## Biology and concepts, with runnable checks

The guides below explain the underlying biology or research concepts, the measurement assumptions, and how to interpret the implemented checks.

| Project | Concept guide | Practical focus |
| --- | --- | --- |
| Enzyme kinetics workbench | [Reaction rates, apparent parameters, and identifiability](https://github.com/TheThunda01/enzyme-kinetics-workbench/blob/main/docs/biology-and-concepts.md) | Nonlinear fitting, parameter profiles, and concentration-range sensitivity |
| Protein structure evidence | [Structures, confidence, residue mapping, and geometric evidence](https://github.com/TheThunda01/protein-structure-evidence/blob/main/docs/biology-and-concepts.md) | Experimental/predicted structure comparison with explicit mapping and evidence limits |
| GFP active learning | [Fluorescence, sequence variation, and retrospective active learning](https://github.com/TheThunda01/gfp-active-learning/blob/main/docs/biology-and-concepts.md) | Budget-matched selection-policy simulations and sequence-aware evaluation |
| Molecular solubility benchmark | [Aqueous solubility, descriptors, and chemical generalization](https://github.com/TheThunda01/molecular-solubility-benchmark/blob/main/docs/biology-and-concepts.md) | Identity/scaffold split comparison and held-out error diagnostics |
| Pasilla expression QC | [RNA processing, gene counts, normalization, and study design](https://github.com/TheThunda01/pasilla-expression-qc/blob/main/docs/biology-and-concepts.md) | Condition/read-type cross-tabulation and additive-design rank diagnostics |
| Sequence Quality Toolkit | [Reads, bases, quality scores, and paired-end data](https://github.com/TheThunda01/sequence-quality-toolkit/blob/main/docs/biology-and-concepts.md) | Streaming checks that paired FASTQ files have matching identities and mate labels |
| Surveillance data quality | [NAAT positivity, test denominators, and reporting time](https://github.com/TheThunda01/surveillance-data-quality/blob/main/docs/biology-and-concepts.md) | Consecutive-week changes in testing denominators, with user-selected review thresholds |
| Cell-feature model validation | [Cell morphology, classification, calibration, and prevalence](https://github.com/TheThunda01/cell-feature-model-validation/blob/main/docs/biology-and-concepts.md) | Conditional predictive-value scenarios under explicitly hypothetical prevalence |
| EvidenceTrail | [Studies, reports, missingness, effects, and certainty](https://github.com/TheThunda01/evidencetrail/blob/main/docs/biology-and-concepts.md) | Field-level source-locator completeness and downloadable summaries |
| Review Compass | [Question framing, retrieval, screening, and synthesis](https://github.com/TheThunda01/review-compass/blob/main/docs/biology-and-concepts.md) | Exact-query structural audit with file fingerprints; search terms retained beyond six entries |

These extensions do not establish biological mechanisms, clinical utility, or validated automated review decisions. The guides explain the specific limits rather than treating a passing software check as scientific confirmation.

## Enzyme kinetics workbench

A curved relationship between substrate concentration and reaction rate can be summarized by a simple model, but a plausible curve does not mean every parameter is well determined. This project uses the archived R Puromycin dataset to explore that distinction through Michaelis–Menten fitting.

It compares the full measured range with low-concentration subsets, inspects residuals, and profiles the apparent parameters. Separate mathematical information scenarios illustrate how the concentration range can affect identifiability under stated assumptions. Key themes are **mechanistic modeling, nonlinear estimation, residuals, parameter uncertainty, and experimental information**. The archived observations are not new laboratory work. Their sparse metadata and units do not support claims about a treatment mechanism, molecular binding affinity, or catalytic turnover.

[Background and sources](https://github.com/TheThunda01/enzyme-kinetics-workbench/blob/main/docs/project-context.md)

## Protein structure evidence

A protein structure is evidence about a molecular arrangement, but it does not directly measure activity or explain every aspect of function. This project compares an experimental carbonic anhydrase II structure with an AlphaFold database prediction to examine what agreement and disagreement can support.

It maps residues between records, superposes comparable coordinates, and summarizes structural displacement and zinc-site geometry. Predicted confidence and experimental displacement parameters are kept separate, and fit choices are made visible. Key themes are **protein structure, residue correspondence, geometric modeling, provenance, and evidence interpretation**. This familiar historical structure is not an independent test of prediction generalization; structural similarity alone does not validate a mechanism or a drug-binding claim.

[Background and sources](https://github.com/TheThunda01/protein-structure-evidence/blob/main/docs/project-context.md)

## GFP active learning

In a learning loop, the next measurements affect what a model can learn. This project explores that idea retrospectively using previously measured variants of green fluorescent protein. A simulated selection policy reveals existing labels rather than generating a new experimental result.

It compares selection strategies under a limited labeling budget and evaluates sequence-based predictions with a separate, more mutated test subset. The focus is how data selection changes learning within this particular pool, not whether a policy can design a useful protein in the laboratory. Key themes are **sequence–phenotype relationships, active learning, acquisition bias, uncertainty, and distribution shift**. The recorded phenotype is assay fluorescence; it is not a direct measurement of isolated-protein stability or organismal fitness. Neither a promising simulation nor model uncertainty establishes prospective performance.

[Background and sources](https://github.com/TheThunda01/gfp-active-learning/blob/main/docs/project-context.md)

## Molecular solubility benchmark

Chemical-property prediction depends on which molecules are available for training and how different the evaluation molecules are. This project uses public aqueous-solubility measurements to compare a training-mean baseline, ridge regression, and a random forest under two structure-based split rules.

It computes descriptors from SMILES, keeps canonical duplicate structures together, and compares identity-grouped random and scaffold-grouped partitions. Model selection stays within training data; held-out error and structural-distance summaries expose limits. Key themes are **cheminformatics, molecular representation, solubility, grouping, and generalization**. Different test sets prevent the split comparison from isolating one causal effect. Missing measurement conditions remain unknown, and solubility is not evidence of potency, safety, or therapeutic utility. The included data retain their noncommercial reuse condition.

[Background and sources](https://github.com/TheThunda01/molecular-solubility-benchmark/blob/main/docs/project-context.md)

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

> **Computational biology and research software portfolio** — Developed and documented Python, SQL, and JavaScript projects exploring enzyme kinetics, protein structures, retrospective active learning, molecular solubility, biological data quality, model evaluation, and evidence-review workflows. Included reproducible examples, automated checks, source attribution, and explicit methodological limitations.

On a detailed CV, list these under Projects or Research Software. Keep them separate from peer-reviewed publications. AI assistance and the distinction between implemented features and future plans are disclosed in the repositories.
