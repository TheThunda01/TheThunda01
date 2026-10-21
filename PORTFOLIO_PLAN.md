# Portfolio roadmap

The portfolio contains thirteen implemented demonstrations. Its four themes are mechanistic and systems modeling, molecular and cellular learning, measurements and statistical validation, and evidence workflows. My interests include AI, protein structure and function, enzyme activity, pathways and interactions, drug discovery and repurposing, host–pathogen biology, and evidence-aware scientific reasoning. The projects develop parts of that foundation; they do not establish expertise across all these areas.

**Portfolio link for a résumé or CV: [github.com/TheThunda01](https://github.com/TheThunda01).** The [project guide](PROJECT_GUIDE.md) explains the rationale and concepts; the [latest expansion](PROJECT_EXPANSION.md) explains the three new questions, implemented analyses, and remaining limits.

The [first practical-use review](RESEARCH_REVIEW.md) and [second verification pass](VERIFICATION_REVIEW.md) record improvements to the original ten projects. Their dated scope remains intact. Project-specific practical-use guides contain remaining work. The [maintenance guide](MAINTENANCE.md) describes a proposed cadence, not an automatic monitoring service.

See the [glossary](docs/glossary.md) for technical terms and the [assumption register](docs/assumptions.md) for collection-level limits.

## Current priority: depth in the GFP investigation

The [four-policy GFP ablation](https://github.com/TheThunda01/gfp-active-learning/blob/main/experiments/uncertainty_ablation/README.md) is implemented, with a fixed plan, matched starting sets and budgets, and a [results report](https://github.com/TheThunda01/gfp-active-learning/blob/main/experiments/uncertainty_ablation/results/report.md). On reused public outcomes across four seeds, diversity-only had the lowest mean distant error and uncertainty-only the lowest mean local error. The recorded prediction favoring the combined policy at distance was not supported. This is an exploratory finding within one fixed comparison.

The priority now is personal understanding and a bounded independent extension, not another repository. The shared learning checkpoints are: explain the methods and result in my own words; develop and document a follow-up before seeing its results; and analyze failures and alternative explanations. These checkpoints are planned, not evidence of work I have already completed independently.

After the GFP checkpoints, the next closed-loop investigation can build on the existing MAPK model, with a prespecified question, matched measurement budgets, and a failure case. A new repository should wait until it serves a question the current projects cannot address.

## Mechanistic and systems modeling

| Project | Status and scope |
| --- | --- |
| [Enzyme kinetics workbench](https://github.com/TheThunda01/enzyme-kinetics-workbench) | Implemented: archived Puromycin data, Michaelis–Menten fits, apparent-parameter profiles, concentration-range sensitivity, and conditional mathematical information scenarios |
| [Yeast flux workbench](https://github.com/TheThunda01/yeast-flux-workbench) | Implemented: pinned Yeast-GEM model, six bound scenarios, selected flux variability, numerical diagnostics, and alternative-solver verification |
| [MAPK dynamics lab](https://github.com/TheThunda01/mapk-dynamics-lab) | Implemented: pinned MAPK model, numerical checks, finite-grid Bayesian updating, three virtual selection policies, and an off-grid stress case |

## Molecular and cellular learning

| Project | Status and scope |
| --- | --- |
| [Protein structure evidence](https://github.com/TheThunda01/protein-structure-evidence) | Implemented: carbonic anhydrase II residue mapping, structure superposition, separate confidence and displacement summaries, zinc-site geometry, and checked coordinate exports |
| [GFP active learning](https://github.com/TheThunda01/gfp-active-learning) | Implemented: provenance-documented fluorescence subset, retrospective acquisition comparisons, separate sequence-shifted evaluation, and final-budget prediction checks |
| [Molecular solubility benchmark](https://github.com/TheThunda01/molecular-solubility-benchmark) | Implemented: attributed solubility data, descriptors, identity/scaffold grouping, training-only model selection, and held-out prediction/error checks |
| [Morphology transfer benchmark](https://github.com/TheThunda01/morphology-transfer-benchmark) | Implemented: raw LINCS profile subset, control normalization, explicit class-support exclusions, compound-held-out retrieval, and simple classification baselines |

## Measurements and statistical validation

| Project | Implemented scope |
| --- | --- |
| [Pasilla expression QC](https://github.com/TheThunda01/pasilla-expression-qc) | Input fingerprints, normalization/PCA sensitivity, condition/read-type diagnostics, numeric output comparison, and an unresolved source-label caveat |
| [Sequence Quality Toolkit](https://github.com/TheThunda01/sequence-quality-toolkit) | Streaming FASTQ checks, paired-file consistency, per-cycle denominators, a public yeast prefix, FASTA/manifest reconciliation, and optional input-lock enforcement |
| [Surveillance data quality](https://github.com/TheThunda01/surveillance-data-quality) | Real CDC snapshot, denominator diagnostics, snapshot comparison, synthetic as-of tests, and typed preflight findings |
| [Cell-feature model validation](https://github.com/TheThunda01/cell-feature-model-validation) | Repeated nested CV, calibration, cross-fitted thresholds, preserved historical holdout results, and candidate-input/feature-declaration checks |

## Evidence and research workflows

| Project | Implemented scope |
| --- | --- |
| [EvidenceTrail](https://github.com/TheThunda01/evidencetrail) | Table checks, comparison coverage, missingness, review decisions, bounded archive verification, and optional comparison with a supplied expected digest |
| [Review Compass](https://github.com/TheThunda01/review-compass) | Review planning, literal keyword cues, query checks, exact-text search records, and explicit predecessor links for revisions |

The thirteen projects use public or clearly labeled synthetic inputs. Their checks do not establish prospective biological validation. Each project remains a bounded demonstration with documented next steps, rather than a finished research program.

## Next learning and research goals

These are proposed milestones, not completed experiments or scheduled commitments. The GFP learning checkpoints above come first; the broader goals below are options for later work.

1. Explain the GFP comparison and its failure cases, then document a personal extension. Gradually apply the same learning checkpoints to the other examples while strengthening programming, mathematics, statistics, and domain knowledge.
2. Build the next closed-loop investigation on the existing MAPK project. Later, extend systems and morphology analyses with independent conditions and suitable external data, as described in [PROJECT_EXPANSION.md](PROJECT_EXPANSION.md). Preserve negative or inconclusive results; adding model complexity is not itself evidence of improvement.
3. Compare mechanistic and statistical models only where a defined question and appropriate measurements justify the comparison. Examine identifiability and distinguish predictions from causal explanations.
4. Explore an experiment–model feedback loop with suitable collaborators and a defined system. Future laboratory work would require an actual protocol, resources, prospective measurements, and independent validation. The current simulations and reanalyses prepare for that goal.
5. Study drug discovery and repurposing with explicit endpoints and suitable validation. Structure, solubility, or morphology scores alone cannot establish binding, efficacy, safety, or clinical benefit.
6. Develop bounded host–pathogen research questions with domain collaborators and appropriate data governance. These case studies do not constitute a host–pathogen investigation.
7. Explore LLMs or agents for literature organization, reasoning support, and research planning with traceable sources and human review. EvidenceTrail and Review Compass are foundations for this interest, not validated autonomous scientific agents.
8. Deepen the foundation projects: add a documented R/Bioconductor analysis, obtain prospective surveillance captures, measure sequence-tool scaling, evaluate suitable independent data, and study realistic review-tool usability.
9. Contribute a useful change to established research software after understanding its methods, contribution guidance, and tests.

## Evidence standard

Use original papers for study findings and official documentation for software behavior and dataset definitions. Keep calculated project results separate from literature claims. Label synthetic examples and retrospective simulations, record source versions and reuse terms, and make failed checks understandable. A passing test does not establish biological correctness, clinical utility, or model generalization.

For each project, be ready to explain why the inputs were chosen, what assumptions were made, what changed under a reasonable alternative, and which parts you personally reviewed and modified. These practices are consistent with [Wilson et al. (2017), Good enough practices in scientific computing](https://doi.org/10.1371/journal.pcbi.1005510). AI assistance is disclosed; understanding and responsibility cannot be delegated to a tool.
