# Brandon J. Huynh

**GitHub portfolio: [github.com/TheThunda01](https://github.com/TheThunda01)**

My interests sit at the intersection of computational biology, AI, mathematical modeling, and experimental molecular biology. My background spans chemistry, molecular laboratory science, epidemiology, and biostatistics. I'm building the computational foundations to connect biological measurements with models that can be questioned, tested, and improved.

My longer-term goal is to develop interpretable models and experimentally testable predictions through an exchange between computation and laboratory evidence. These complementary case studies explore parts of that goal; they do not report experiments that I conducted or establish new biological findings.

The collection contains thirteen runnable projects. The [latest expansion](PROJECT_EXPANSION.md) adds metabolic networks, signaling dynamics, and cellular phenotypes to the earlier molecular and data-quality examples.

My current focus is depth: understanding the [GFP policy ablation](https://github.com/TheThunda01/gfp-active-learning/blob/main/experiments/uncertainty_ablation/README.md) and developing a personal extension I can explain and defend. The completed four-policy comparison did not support the recorded prediction that the combined policy would help most on more-distant variants. Diversity-only had the lowest mean distant error, and uncertainty-only the lowest mean local error, across four seeds on reused public outcomes. The [results report](https://github.com/TheThunda01/gfp-active-learning/blob/main/experiments/uncertainty_ablation/results/report.md) keeps that exploratory scope visible.

The next checkpoints are my own explanation of the result, an independently developed extension, and a failure analysis; these are goals, not completed claims. After that, the existing MAPK project offers a place to deepen closed-loop modeling before considering another repository.

## Mechanistic and systems modeling

| Project | Question and approach |
| --- | --- |
| [Enzyme kinetics workbench](https://github.com/TheThunda01/enzyme-kinetics-workbench) | What can a small kinetic dataset identify? Nonlinear fitting, apparent parameters, and concentration-range sensitivity. |
| [Yeast flux workbench](https://github.com/TheThunda01/yeast-flux-workbench) | Which flux conclusions depend on model constraints? A pinned yeast model, flux balance analysis, and feasible flux ranges. |
| [MAPK dynamics lab](https://github.com/TheThunda01/mapk-dynamics-lab) | Which simulated observations help distinguish parameter hypotheses? Pathway dynamics, Bayesian updating, and virtual observation selection. |

## Molecular and cellular learning

| Project | Question and approach |
| --- | --- |
| [Protein structure evidence](https://github.com/TheThunda01/protein-structure-evidence) | What does structural agreement support? Residue mapping, geometric comparison, and separate confidence measures. |
| [GFP active learning](https://github.com/TheThunda01/gfp-active-learning) | How do selection policies use a labeling budget? Retrospective fluorescence simulations and sequence-aware evaluation. |
| [Molecular solubility benchmark](https://github.com/TheThunda01/molecular-solubility-benchmark) | How does chemical separation change evaluation? Descriptor models, grouped splits, and held-out errors. |
| [Morphology transfer benchmark](https://github.com/TheThunda01/morphology-transfer-benchmark) | What transfers to unseen compounds? Public Cell Painting profiles, compound-held-out retrieval, and simple classification baselines. |

## Measurements and statistical validation

| Project | Question and approach |
| --- | --- |
| [Pasilla expression QC](https://github.com/TheThunda01/pasilla-expression-qc) | How sensitive are sample relationships? Public counts, metadata checks, normalization, and PCA sensitivity. |
| [Sequence Quality Toolkit](https://github.com/TheThunda01/sequence-quality-toolkit) | What should be checked first? Streaming FASTQ validation, paired-read checks, and quality summaries. |
| [Surveillance data quality](https://github.com/TheThunda01/surveillance-data-quality) | What supports a surveillance summary? Denominators, captured releases, and synthetic revision histories. |
| [Cell-feature model validation](https://github.com/TheThunda01/cell-feature-model-validation) | What lies beyond one model score? Nested evaluation, calibration, and threshold development. |

## Evidence and research workflows

| Project | Question and approach |
| --- | --- |
| [EvidenceTrail](https://github.com/TheThunda01/evidencetrail) | How can extraction records be inspected? Coverage, missingness, review decisions, and archive checks. |
| [Review Compass](https://github.com/TheThunda01/review-compass) | How can a review plan be traced? Planning, literal keyword cues, query checks, and recorded revisions. |

The [project guide](PROJECT_GUIDE.md) explains background and concepts; the [roadmap](PORTFOLIO_PLAN.md) separates implemented work from research goals. The repositories include runnable instructions, methods, sources, and limitations. Public-data analyses, simulations, and proposed future experiments are identified separately.

The [research review](RESEARCH_REVIEW.md), [verification update](VERIFICATION_REVIEW.md), [shared standard](PORTFOLIO_STANDARDS.md), and [maintenance guide](MAINTENANCE.md) record how I approach evidence and reproducibility.

These projects were developed with AI assistance. Public data retain attribution and reuse terms; synthetic examples are labeled. Tests check specified behavior, not biological correctness, clinical validity, or autonomous scientific judgment. I welcome feedback on questions and methods I can explain and reproduce.
