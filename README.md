# Brandon J. Huynh, MPH

**Molecular laboratory scientist exploring computational biology and mathematical modeling.**

I'm building computational skills to connect biological measurements with models that can be questioned, tested, and improved. My background spans chemistry, molecular laboratory science, epidemiology, and biostatistics. My interests include artificial intelligence (AI) and experimental molecular biology.

These thirteen projects use public data and simulations to explore that connection. They support my longer-term goal of developing interpretable models and experimentally testable predictions; they do not report new laboratory experiments I conducted or establish new biological findings.

My current focus is the [green fluorescent protein (GFP) policy comparison](https://github.com/TheThunda01/gfp-active-learning/blob/main/experiments/uncertainty_ablation/README.md). It separates the components of a selection method to test what each contributes, an approach called *ablation*. Across four random-number seeds, diversity-only selection had the lowest mean error on more-distant sequence variants, and uncertainty-only selection had the lowest mean error on local variants. The comparison did not support the prediction that the combined policy would help most at distance. These [exploratory results](https://github.com/TheThunda01/gfp-active-learning/blob/main/experiments/uncertainty_ablation/results/report.md) reuse public outcomes and do not establish a general winning policy.

My next goals are to explain that result in my own words, develop an independent extension, and analyze failures. After those checkpoints, I plan to deepen the existing mitogen-activated protein kinase (MAPK) project, where simulated observations guide the next measurement choice. The [project guide](PROJECT_GUIDE.md) explains the collection; the [roadmap](PORTFOLIO_PLAN.md) separates implemented work from these future goals.

## Start here

| If you want to explore… | Start with | What to look for |
| --- | --- | --- |
| How a result changes the next question | [GFP policy comparison](https://github.com/TheThunda01/gfp-active-learning/blob/main/experiments/uncertainty_ablation/README.md) | A recorded prediction, an unexpected result, and the limits of what it explains. |
| How models guide measurement choices | [MAPK dynamics](https://github.com/TheThunda01/mapk-dynamics-lab) | A small mechanistic model, competing observation schedules, and a simulation stress test. |
| How assumptions affect biological data analysis | [Pasilla expression QC](https://github.com/TheThunda01/pasilla-expression-qc) | Normalization and sample-influence checks, with an unresolved source-label discrepancy kept visible. |

The [maintenance review](docs/review-2026-10-26.md) records accuracy and reproducibility checks; the [writing review](docs/writing-review-2026-10-26.md) explains the revisions based on *Writing in the Sciences*. The project lists below give a broader route through the work.

## Mechanistic and systems modeling

| Project | What it explores |
| --- | --- |
| [Enzyme kinetics workbench](https://github.com/TheThunda01/enzyme-kinetics-workbench) | Fits enzyme rates and tests how concentration range affects apparent parameters. |
| [Yeast flux workbench](https://github.com/TheThunda01/yeast-flux-workbench) | Uses a pinned yeast model to test how constraints affect feasible metabolic fluxes. |
| [MAPK dynamics lab](https://github.com/TheThunda01/mapk-dynamics-lab) | Compares virtual measurement schedules for distinguishing parameter hypotheses in a signaling model. |

## Molecular and cellular learning

| Project | What it explores |
| --- | --- |
| [Protein structure evidence](https://github.com/TheThunda01/protein-structure-evidence) | Compares experimental and predicted protein structures while separating geometric agreement from confidence and displacement measures. |
| [GFP active learning](https://github.com/TheThunda01/gfp-active-learning) | Compares label-selection policies retrospectively using measured fluorescence and sequence-aware evaluation. |
| [Molecular solubility benchmark](https://github.com/TheThunda01/molecular-solubility-benchmark) | Tests descriptor models on chemical groups held out from training. |
| [Morphology transfer benchmark](https://github.com/TheThunda01/morphology-transfer-benchmark) | Tests retrieval and simple classifiers on held-out compounds using public Cell Painting profiles. |

## Measurements and statistical validation

| Project | What it explores |
| --- | --- |
| [Pasilla expression QC](https://github.com/TheThunda01/pasilla-expression-qc) | Checks how normalization and sample influence affect RNA-seq quality control (QC). |
| [Sequence Quality Toolkit](https://github.com/TheThunda01/sequence-quality-toolkit) | Validates FASTQ sequence-and-quality files, checks paired reads, and summarizes quality. |
| [Surveillance data quality](https://github.com/TheThunda01/surveillance-data-quality) | Audits denominators and captured releases, and explores synthetic revision histories. |
| [Cell-feature model validation](https://github.com/TheThunda01/cell-feature-model-validation) | Examines model evaluation, calibration, and threshold development on a public cell-feature dataset. |

## Evidence and research workflows

| Project | What it explores |
| --- | --- |
| [EvidenceTrail](https://github.com/TheThunda01/evidencetrail) | Checks extraction records, comparison coverage, missingness, review decisions, and exported archives. |
| [Review Compass](https://github.com/TheThunda01/review-compass) | Organizes review plans, shows literal keyword cues, checks queries, and records revisions. |

Each repository includes runnable instructions, methods, sources, and limitations. The [systems and cellular expansion](PROJECT_EXPANSION.md) explains how the three newest projects extend the collection. The [shared standard](PORTFOLIO_STANDARDS.md) and [maintenance guide](MAINTENANCE.md) describe the approach to evidence and reproducibility.

Use the [glossary](docs/glossary.md) for unfamiliar terms, the [assumptions](docs/assumptions.md) for limits on the claims, and the [references](REFERENCES.md) and [reference audit](docs/reference-audit.json) for source details and access limits. Earlier checks remain in the [research review](RESEARCH_REVIEW.md), [verification update](VERIFICATION_REVIEW.md), [21 October review](docs/review-2026-10-21.md), and [20 October review](docs/review-2026-10-20.md).

These projects were developed with AI assistance. Public data retain attribution and reuse terms; synthetic examples are labeled. Tests check specified behavior, not biological correctness, clinical validity, or autonomous scientific judgment. I welcome feedback on questions and methods I can explain and reproduce.
