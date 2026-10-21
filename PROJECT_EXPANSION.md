# From molecular examples to systems and cellular responses

The latest three projects add coupled metabolic networks, time-dependent signaling, and cellular morphology to the portfolio. Each has an executable analysis, public inputs with reuse terms, worked results, biological explanations, and repeatable checks. This page describes their implemented scope as of 20 October 2026.

My aim is to connect biological measurements, mechanistic models, and statistical learning in ways I can explain and reproduce. These projects use different systems. They do not report laboratory experiments that I conducted or form one experimentally validated discovery pipeline.

The [glossary](docs/glossary.md) explains the technical terms below; each linked project has its own assumptions and source audit.

## What each project adds

| Project | Scientific question | Concepts | Practical role and boundary |
| --- | --- | --- | --- |
| [Yeast flux workbench](https://github.com/TheThunda01/yeast-flux-workbench) | Which growth and flux conclusions remain feasible under declared resource bounds? | Stoichiometry, linear optimization, feasible sets, alternative solutions | Inspect a public metabolic model and its assumptions; simulated fluxes are not measurements |
| [MAPK dynamics lab](https://github.com/TheThunda01/mapk-dynamics-lab) | Which simulated observations help distinguish parameter hypotheses? | Differential equations, feedback, Bayesian inference, identifiability | Compare sequential observation rules under an explicit model and noise scenario; no laboratory validation is implied |
| [Morphology transfer benchmark](https://github.com/TheThunda01/morphology-transfer-benchmark) | Do profiles recover annotated relationships for compounds withheld from development? | Phenotypic profiling, control normalization, grouped evaluation, confounding | Audit public profiles and compare retrieval and simple classifiers; a similar phenotype is not proof of a shared mechanism |

The enzyme workbench examines a small rate equation. Yeast adds network constraints; MAPK adds time courses and feedback. GFP active learning reveals archived sequence labels, while MAPK studies a generative mathematical model. Morphology adds cellular responses to the solubility project's chemical-property endpoint. Those differences give each repository a distinct question.

## Yeast flux workbench

The input is the official [yeast-GEM v9.1.1 release](https://github.com/SysBioChalmers/yeast-GEM/releases/tag/v9.1.1), retained under its CC BY 4.0 terms. [Zhang et al. (2024)](https://pubmed.ncbi.nlm.nih.gov/39134886/) describe the Yeast9 model ecosystem. The pinned snapshot's dimensions and constraints are checked by code; its contents need not match the earlier paper's release exactly.

The analysis varies oxygen uptake while keeping other medium assumptions explicit. Five feasible scenarios and a zero-glucose diagnostic illustrate usable solutions and infeasibility. Selected flux variability calculations examine how much freedom remains near the growth optimum. Saved flux vectors are checked for balance and bounds, and extrema are compared with a different HiGHS algorithm.

The exact optimum is numerically delicate. The effective growth floor and numerical slack are recorded rather than hidden behind an apparent 100% requirement. Feasible ranges are not confidence intervals or a joint distribution over fluxes. They can include internal cycles and depend on bounds, the biomass objective, and omitted kinetic or regulatory constraints. Lowering oxygen alone does not establish an anaerobic model or reproduce the Crabtree effect.

A useful next step would compare results with suitably matched independent flux measurements, accounting for measurement uncertainty and model-condition alignment. Enzyme-capacity and regulatory extensions should be assessed separately.

## MAPK dynamics lab

The input is the CC0 [BioModels BIOMD0000000010 encoding](https://github.com/biomodels/BIOMD0000000010/tree/d95a205b39b7e5bdc172a368534cda60c74ab420) of the feedback model described by [Kholodenko (2000)](https://pubmed.ncbi.nlm.nih.gov/10712587/). The implementation checks its eight species, ten reaction rates, conserved totals, source equations, and agreement between numerical formulations.

The learning experiment compares 49 hypotheses over two parameter directions, holding other parameters fixed. Twenty matched-model seeds compare variance-guided, random, and fixed observation schedules with the same 12-observation budget. Six off-grid noise repeats examine one way the finite hypothesis set can be wrong: the true values fall between discrete candidates while remaining inside their parameter ranges. This tests discretization, not extrapolation beyond those ranges. Observation, selection, posterior, and metric tables make the result inspectable.

The variance-guided rule performs better on average in the committed matched-model example. This is a bounded simulation result: its score is posterior-weighted prediction variance, not exact expected information gain or proof of an optimal design. The posterior depends on the grid, noise model, and fixed parameters. [Blüthgen et al. (2006)](https://pubmed.ncbi.nlm.nih.gov/16478465/) show why omitted enzyme–substrate sequestration can change this model class's dynamics. An internally consistent trajectory does not confirm that real cells follow these equations.

A useful extension would compare alternative model structures, observable definitions, and noise assumptions before adapting the approach to an experimental dataset.

## Morphology transfer benchmark

The source is [LINCS Cell Painting](https://github.com/broadinstitute/lincs-cell-painting/tree/061870127481dcd73c29df85ebcfddeac2ed0828), whose data have CC0 terms. A compact snapshot retains 3,674 wells and 72 prespecified shape/intensity features, including negative controls for plate normalization. The source-object manifest records the inspected profiles and filtering decisions.

Eight mechanism classes were selected before model scores were computed. Seven satisfy the declared support rule after profile and quality checks, leaving 76 related-compound groups. The fixed split has 48 training, 14 validation, and 14 test groups. The low-support class remains visible in the audit. Related identities and replicate wells stay together; preprocessing uses training compounds after explicit DMSO-only plate normalization.

Retrieval uses a training reference gallery, excluding the query's related identity and any shared plate map. It records valid-reference counts and ineligible queries. Simple classification baselines select settings using validation data. With only 14 test groups, one changed prediction moves accuracy by about seven percentage points; these results cannot establish broad model superiority. Plate/position effects, annotation quality, and the restricted panel remain important limits. A source dose-field naming discrepancy is preserved and discussed rather than silently converted into a concentration claim.

A useful next step would use an external experiment or batch with compatible controls, annotations, and enough independent compounds. A larger model would need justification from that evaluation.

## How the thirteen projects fit together

| Theme | Projects |
| --- | --- |
| Mechanistic and systems modeling | Enzyme kinetics; yeast flux; MAPK dynamics |
| Molecular and cellular learning | Protein structure; GFP active learning; molecular solubility; morphology transfer |
| Measurements and statistical validation | Sequence QC; expression QC; surveillance data; cell-feature validation |
| Evidence and research workflows | EvidenceTrail; Review Compass |

The [project guide](PROJECT_GUIDE.md) explains the biology and rationale across the collection. Each new repository includes a dated, bounded literature search, practical-use guide, input provenance, limitations, and further work. These records support traceability; they are not exhaustive systematic reviews. Earlier [research](RESEARCH_REVIEW.md) and [verification](VERIFICATION_REVIEW.md) records retain their original ten-project scope.

The [roadmap](PORTFOLIO_PLAN.md) keeps future wet-lab collaboration, host–pathogen research, and evidence-aware agents separate from current capabilities. All three additions were developed with AI assistance. Reproducing and explaining their assumptions is part of the work, not something a passing test can replace.
