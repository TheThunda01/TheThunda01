# A quick guide to the projects

These fourteen projects explore biological modeling, machine learning, measurement quality, and evidence workflows. Each repository contains a runnable demonstration with documented inputs, methods, and limits.

The projects reflect my interests in computational biology, artificial intelligence (AI), mathematical modeling, and experimental molecular biology. They use different systems and datasets to develop complementary skills. They do not form a validated pipeline or report new laboratory experiments I conducted or mechanisms I established.

**For a résumé or CV: [github.com/TheThunda01](https://github.com/TheThunda01).**

The [systems and cellular expansion](PROJECT_EXPANSION.md) explains what those projects add and where they still need development. The [research review](RESEARCH_REVIEW.md) and [verification update](VERIFICATION_REVIEW.md) preserve the earlier ten-project review history. The [shared standard](PORTFOLIO_STANDARDS.md) describes the documentation expected before a new project is presented as complete.

The [glossary](docs/glossary.md) defines the terms below, including green fluorescent protein (GFP), mitogen-activated protein kinase (MAPK), and the statistical methods. The [assumption register](docs/assumptions.md) explains the scope of the collection.

## Current learning investigation: GFP

The [completed policy ablation](https://github.com/TheThunda01/gfp-active-learning/blob/main/experiments/uncertainty_ablation/README.md) tests what each component of a selection method contributes. It compares random, uncertainty-only, diversity-only, and combined selection with the same starting labels, budgets, and model.

Across four random-number seeds, diversity-only had the lowest mean error on more-distant sequence variants, and uncertainty-only had the lowest mean error on local variants. The comparison did not support the recorded prediction that combined selection would help most at distance. These results reuse public outcomes; they are exploratory, not a new blind evaluation or evidence of a universal winning policy. See the [report](https://github.com/TheThunda01/gfp-active-learning/blob/main/experiments/uncertainty_ablation/results/report.md).

The next learning checkpoints remain to be completed:

- **Personal explanation:** explain why the comparison is fair, what the error and disagreement measures mean, and what the result does not establish.
- **Independent extension:** develop one bounded follow-up, write the expected outcome and comparison before running it, and identify the decisions and code I contributed.
- **Failure analysis:** inspect where the model or selection rule fails, test a competing explanation, and retain negative or inconclusive results.

Once those checkpoints are complete, deepen the existing MAPK closed-loop simulation with a defined question and failure case before adding a repository.

## Biology and concepts

The guides explain the biological measurements, model assumptions, and implemented checks.

| Project | Concept guide | Practical focus |
| --- | --- | --- |
| Enzyme kinetics workbench | [Reaction rates, apparent parameters, and identifiability](https://github.com/TheThunda01/enzyme-kinetics-workbench/blob/main/docs/biology-and-concepts.md) | Nonlinear fitting, parameter profiles, and concentration-range sensitivity |
| Protein structure evidence | [Structures, confidence, residue mapping, and geometric evidence](https://github.com/TheThunda01/protein-structure-evidence/blob/main/docs/biology-and-concepts.md) | Experimental/predicted structure comparison with explicit mapping and evidence limits |
| Nature's Perfume Lab | [Terpene chemistry, atom correspondence and enzyme evidence](https://github.com/TheThunda01/natures-perfume-lab/blob/main/docs/biology-and-concepts.md) | Attributed chemical graphs, curated carbon labels, sequence alignment and structural coverage |
| GFP active learning | [Fluorescence, sequence variation, and retrospective active learning](https://github.com/TheThunda01/gfp-active-learning/blob/main/docs/biology-and-concepts.md) | Budget-matched selection-policy simulations and sequence-aware evaluation |
| Molecular solubility benchmark | [Aqueous solubility, descriptors, and chemical generalization](https://github.com/TheThunda01/molecular-solubility-benchmark/blob/main/docs/biology-and-concepts.md) | Identity/scaffold split comparison and held-out error diagnostics |
| Pasilla expression QC | [RNA processing, gene counts, normalization, and study design](https://github.com/TheThunda01/pasilla-expression-qc/blob/main/docs/biology-and-concepts.md) | Condition/read-type cross-tabulation and additive-design rank diagnostics |
| Sequence Quality Toolkit | [Reads, bases, quality scores, and paired-end data](https://github.com/TheThunda01/sequence-quality-toolkit/blob/main/docs/biology-and-concepts.md) | Streaming checks that paired FASTQ files have matching identities and mate labels |
| Surveillance data quality | [NAAT positivity, test denominators, and reporting time](https://github.com/TheThunda01/surveillance-data-quality/blob/main/docs/biology-and-concepts.md) | Consecutive-week changes in testing denominators, with user-selected review thresholds |
| Cell-feature model validation | [Cell morphology, classification, calibration, and prevalence](https://github.com/TheThunda01/cell-feature-model-validation/blob/main/docs/biology-and-concepts.md) | Conditional predictive-value scenarios under explicitly hypothetical prevalence |
| EvidenceTrail | [Studies, reports, missingness, effects, and certainty](https://github.com/TheThunda01/evidencetrail/blob/main/docs/biology-and-concepts.md) | Field-level source-locator completeness and downloadable summaries |
| Review Compass | [Question framing, retrieval, screening, and synthesis](https://github.com/TheThunda01/review-compass/blob/main/docs/biology-and-concepts.md) | Exact-query structural audit with file fingerprints; search terms retained beyond six entries |
| Yeast flux workbench | [Metabolism and flux guide](https://github.com/TheThunda01/yeast-flux-workbench/blob/main/docs/biology-and-concepts.md) | Constraint-based network modeling, selected flux ranges, and solver checks |
| MAPK dynamics lab | [Dynamics and information guide](https://github.com/TheThunda01/mapk-dynamics-lab/blob/main/docs/biology-and-concepts.md) | Time courses, feedback, Bayesian updating, and virtual observations |
| Morphology transfer benchmark | [Morphology and transfer guide](https://github.com/TheThunda01/morphology-transfer-benchmark/blob/main/docs/biology-and-concepts.md) | Control-normalized public profiles and compound-level retrieval/evaluation |

## Mechanistic and systems modeling

### Enzyme kinetics workbench

A model can fit reaction rates well while leaving its parameters uncertain. This project explores that distinction by fitting the Michaelis–Menten model to the archived R Puromycin dataset.

It compares the full measured range with low-concentration subsets, inspects residuals, and profiles the apparent parameters. Separate mathematical information scenarios illustrate how the concentration range can affect identifiability under stated assumptions.

The archived observations are not new laboratory work. Their sparse metadata and units do not support claims about a treatment mechanism, molecular binding affinity, or catalytic turnover.

[Background and sources](https://github.com/TheThunda01/enzyme-kinetics-workbench/blob/main/docs/project-context.md)

### Yeast flux workbench

Metabolic reactions share substrates and products, so a change in one part of a network can constrain other pathways. This project asks which growth and exchange-flux conclusions remain feasible when oxygen uptake and the required growth fraction change. It extends the portfolio from individual-enzyme kinetics to network modeling.

The implementation uses a pinned Yeast-GEM v9.1.1 snapshot, sparse linear optimization, and selected-reaction flux variability analysis. Six declared scenarios include a deliberately infeasible diagnostic. The workflow checks saved fluxes against balance equations and bounds, then compares extrema using a different solver algorithm.

Feasible ranges are not confidence intervals or measured fluxes; the published model's performance does not automatically validate this analysis.

[Background and sources](https://github.com/TheThunda01/yeast-flux-workbench/blob/main/docs/project-context.md)


### MAPK dynamics lab

Signaling pathways change over time, and similar-looking trajectories can leave several parameter explanations open. This project asks which simulated observations help distinguish those explanations in a compact, published MAPK cascade.

It translates a pinned BioModels encoding, checks conservation and numerical agreement, and updates a finite grid of two-parameter hypotheses. The simulation compares a variance-guided selection rule with random and fixed schedules under the same virtual measurement budget. An off-grid case, with true values between candidates but inside their parameter ranges, exposes the limitations of a finite hypothesis set.

All observations are simulated. The acquisition rule is a heuristic, and successful recovery within this model does not validate a real signaling mechanism or laboratory experiment.

[Background and sources](https://github.com/TheThunda01/mapk-dynamics-lab/blob/main/docs/project-context.md)


## Molecular and cellular learning

### Protein structure evidence

A protein structure is evidence about a molecular arrangement, but it does not directly measure activity or explain every aspect of function. This project compares an experimental carbonic anhydrase II structure with an AlphaFold database prediction to examine what agreement and disagreement can support.

It maps residues between records, superposes comparable coordinates, and summarizes structural displacement and zinc-site geometry. The analysis separates predicted confidence from experimental displacement parameters and records the fitting choices.

This familiar historical structure is not an independent test of prediction generalization; structural similarity alone does not validate a mechanism or a drug-binding claim.

[Background and sources](https://github.com/TheThunda01/protein-structure-evidence/blob/main/docs/project-context.md)

### Nature's Perfume Lab

How can a shared starting molecule lead to different plant aroma compounds? This fixed case follows geranyl diphosphate toward the selected limonene and linalool products, links curated carbon labels to attributed chemical graphs, and compares two documented enzyme sequences.

The explorer and Python workflow keep chemical identity, alignment denominators and the citrus structure's coverage inspectable. Carbon labels record a curated correspondence rather than measured atom fate. The project does not compare matched enzyme pockets or predict scent perception, and it includes no new laboratory or sensory measurements.

[Background and sources](https://github.com/TheThunda01/natures-perfume-lab/blob/main/docs/project-context.md)

### GFP active learning

The choice of the next measurement affects what a model can learn. This project explores that choice retrospectively using previously measured variants of green fluorescent protein. A simulated selection policy reveals existing labels; it does not generate new experimental results.

It compares selection strategies under a limited labeling budget and evaluates sequence-based predictions with a separate, more mutated test subset. The focus is how data selection changes learning within this particular pool, not whether a policy can design a useful protein in the laboratory.

The recorded phenotype is assay fluorescence; it is not a direct measurement of isolated-protein stability or organismal fitness. Neither a promising simulation nor model uncertainty establishes prospective performance.

[Background and sources](https://github.com/TheThunda01/gfp-active-learning/blob/main/docs/project-context.md)

### Molecular solubility benchmark

Chemical-property prediction depends on which molecules are available for training and how different the evaluation molecules are. This project uses public aqueous-solubility measurements to compare a training-mean baseline, ridge regression, and a random forest under two structure-based split rules.

It computes descriptors from SMILES, keeps canonical duplicate structures together, and compares identity-grouped random and scaffold-grouped partitions. Model selection stays within training data; held-out error and structural-distance summaries expose limits.

Different test sets prevent the split comparison from isolating one causal effect. Missing measurement conditions remain unknown, and solubility is not evidence of potency, safety, or therapeutic utility. The included data retain their noncommercial reuse condition.

[Background and sources](https://github.com/TheThunda01/molecular-solubility-benchmark/blob/main/docs/project-context.md)

### Morphology transfer benchmark

Cellular morphology provides an indirect view of a cell's response to a perturbation. This project asks whether public image-derived profiles can recover annotated relationships between compounds withheld from model development. It complements chemical-property prediction by studying a cellular phenotype.

A compact LINCS Cell Painting subset preserves raw well-level measurements and DMSO controls. The workflow audits annotations and support, groups related chemical identities, normalizes each relevant plate using its DMSO controls, fits subsequent preprocessing on training compounds, and evaluates retrieval and simple classifiers. Seven supported mechanism classes remain from eight prespecified candidates; exclusions stay visible.

Retrieval excludes shared identities and plate maps. The classifier still faces plate and position confounding, and a similar phenotype does not establish a direct target, mechanism, or therapeutic benefit.

[Background and sources](https://github.com/TheThunda01/morphology-transfer-benchmark/blob/main/docs/project-context.md)


## Measurements and statistical validation

### Pasilla expression QC

Gene-count tables are not ready-made biological answers. Library size, count composition, sample annotation, and transformation choices can affect exploratory views. This project uses public Drosophila counts to investigate those choices before asking a gene-level question.

It checks sample identifiers, summarizes counts, compares total-count and median-ratio normalization, and refits PCA after omitting each sample. The sensitivity analysis identifies influential samples for investigation rather than automatic deletion.

It does not perform differential-expression testing or reproduce the original splicing study.

[Background and sources](https://github.com/TheThunda01/pasilla-expression-qc/blob/main/docs/project-context.md)

### Sequence Quality Toolkit

Sequence formats look simple, but malformed records, mismatched metadata, ambiguous symbols, and misunderstood quality scores can quietly undermine downstream work. This command-line toolkit checks file structure, metadata, and sequence quality.

It streams FASTQ files, validates record structure, calculates per-read and per-cycle quality summaries, and checks FASTA records against sample manifests. A documented 1,000-read prefix from a public yeast RNA-seq run complements synthetic edge cases.

The prefix cannot characterize the complete run, and quality scores are predictions rather than observed error measurements.

[Background and sources](https://github.com/TheThunda01/sequence-quality-toolkit/blob/main/docs/project-context.md)

### Surveillance data quality

A surveillance curve can hide missing submissions, changing denominators, or later revisions. This project audits the records behind the curve before interpreting its shape.

It audits a pinned CDC aggregate extract, checks counts and displayed percentages, compares snapshots, and uses synthetic report histories to reconstruct information available by a stated date.

A complete extract is not proof of complete population coverage; one real snapshot cannot reveal historical reporting delays.

[Background and sources](https://github.com/TheThunda01/surveillance-data-quality/blob/main/docs/project-context.md)

### Cell-feature model validation

A classifier can achieve a strong benchmark score without establishing that it will help in a new setting. This project uses a public cell-image-feature dataset to examine evaluation choices rather than claim a clinical application.

It compares logistic regression, a small random forest, and a prior baseline using repeated nested cross-validation. It develops thresholds from training data and describes their performance on a previously observed holdout. Calibration and uncertainty summaries state the limits of that evaluation.

The holdout is not newly blinded validation, and benchmark performance does not establish clinical utility.

[Background and sources](https://github.com/TheThunda01/cell-feature-model-validation/blob/main/docs/project-context.md)

## Evidence and research workflows

### EvidenceTrail

EvidenceTrail helps reviewers trace extraction records and inspect disagreements. It checks record structure while leaving scientific interpretation to the reviewer.

EvidenceTrail checks tables, compares reviewer records, shows how many submitted rows could be paired, and separates nonblank text agreement from missing entries. It records review decisions and exports the result.

Matching text is not proof that an answer is correct or scientifically supported.

[Background and sources](https://github.com/TheThunda01/evidencetrail/blob/main/docs/project-context.md)

### Review Compass

Review Compass keeps a review question, eligibility criteria, search ideas, and unresolved decisions in one place. Its automated cues help reviewers inspect text without making screening decisions for them.

It organizes a review plan, displays literal keyword matches for manual inspection, and exports planning notes. Field-completion counts describe what was entered; they do not score methodological quality.

Keyword cues cannot determine eligibility or understand negation and study design.

[Background and sources](https://github.com/TheThunda01/review-compass/blob/main/docs/project-context.md)

## Presenting the work on a résumé or CV

Put [github.com/TheThunda01](https://github.com/TheThunda01) in the contact header. For a role with a particular focus, link one or two relevant repositories beside the project entries so the reader does not have to search. Use claims you can explain and demonstrate yourself.

Example wording, after reviewing and reproducing the work:

> **Computational biology and research software portfolio** — Developed and documented Python, SQL, and JavaScript projects exploring molecular and systems biology, virtual experimental design, phenotype learning, biological data quality, and evidence-review workflows. Included reproducible examples, automated checks, source attribution, and explicit methodological limitations.

On a detailed CV, list these under Projects or Research Software. Keep them separate from peer-reviewed publications. AI assistance and the distinction between implemented features and future plans are disclosed in the repositories.
