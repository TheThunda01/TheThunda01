# Portfolio roadmap

The direction is **from biological measurements to better experiments**: examine the inputs, test what a model can support, and investigate which observation would help next. The current priority is a focused follow-up to the GFP selection-policy comparison, followed by a deeper MAPK failure analysis.

The [project guide](PROJECT_GUIDE.md) gives a reading path through all fourteen demonstrations. Enzyme kinetics is the introduction, GFP is the current investigation, and MAPK is the next research direction. The supporting projects supply measurement checks, evaluation methods, evidence workflows, and an accessible visual example. They use different systems and do not form an integrated discovery pipeline.

## Current priority: depth in the GFP investigation

**Completed:** The [four-policy ablation](https://github.com/TheThunda01/gfp-active-learning/blob/main/experiments/uncertainty_ablation/README.md) compares selection rules using matched starting sets and budgets. Across four seeds, diversity-only had the lowest mean distant error and uncertainty-only the lowest mean local error. The combined policy did not support the prediction that it would help most at distance. These are exploratory findings on reused public outcomes.

**Proposed next question:** Does the combined policy's uncertainty shortlist exclude candidates that the full-pool diversity rule selects?

Before running the extension, specify the candidate-pool comparison, expected outcome, measurement budgets, and evaluation plan. Keep the existing results intact. Inspect selected candidates and error patterns, compare a competing explanation, and report negative or inconclusive findings. This is a planned analysis, not an established explanation for the current result.

**Completion evidence:** a recorded plan, reproducible comparison, candidate-selection diagnostics, interpretation tied to the observed results, and a contribution record describing the decisions and implementation changes.

## Next direction: MAPK measurement selection

**Completed:** The existing simulation compares three observation schedules and includes an off-grid case in which the hidden parameters lie between the candidate values.

**Proposed next question:** Under which model or observation assumptions does the apparent advantage of measurement selection disappear?

Extend one declared failure case with matched budgets and an appropriate baseline. Distinguish errors caused by a finite parameter grid from changes to the model structure or observation process. The current simulation has not established how the method performs in a laboratory.

**Completion evidence:** a question and comparison specified before the new run, preserved baseline outputs, reproducible sensitivity results, and a report explaining both useful and unsuccessful observation choices.

## Implemented project inventory

The groups below describe each project's role in the story, not a ranking of scientific validity. Each project's practical-use guide retains its detailed limitations and improvement criteria.

<a id="mechanistic-and-systems-modeling"></a>

### Featured studies

| Project | Implemented scope |
| --- | --- |
| [Enzyme kinetics workbench](https://github.com/TheThunda01/enzyme-kinetics-workbench) | Implemented: archived Puromycin data, Michaelis–Menten fits, apparent-parameter profiles, concentration-range sensitivity, and conditional mathematical information scenarios |
| [GFP active learning](https://github.com/TheThunda01/gfp-active-learning) | Implemented: provenance-documented fluorescence subset, retrospective acquisition comparisons, separate sequence-shifted evaluation, and final-budget prediction checks |
| [MAPK dynamics lab](https://github.com/TheThunda01/mapk-dynamics-lab) | Implemented: pinned MAPK model, numerical checks, finite-grid Bayesian updating, three virtual selection policies, and an off-grid stress case |

<a id="measurements-and-statistical-validation"></a>

### Measurement foundations

| Project | Implemented scope |
| --- | --- |
| [Surveillance data quality](https://github.com/TheThunda01/surveillance-data-quality) | Real CDC snapshot, denominator diagnostics, snapshot comparison, synthetic as-of tests, and typed preflight findings |
| [Sequence Quality Toolkit](https://github.com/TheThunda01/sequence-quality-toolkit) | Streaming FASTQ checks, paired-file consistency, per-cycle denominators, a public yeast prefix, FASTA/manifest reconciliation, and optional input-lock enforcement |
| [Pasilla expression QC](https://github.com/TheThunda01/pasilla-expression-qc) | Input fingerprints, normalization/PCA sensitivity, condition/read-type diagnostics, numeric output comparison, and an unresolved source-label caveat |

<a id="molecular-and-cellular-learning"></a>

### Testing models and assumptions

| Project | Implemented scope |
| --- | --- |
| [Cell-feature model validation](https://github.com/TheThunda01/cell-feature-model-validation) | Repeated nested CV, calibration, cross-fitted thresholds, preserved historical holdout results, and candidate-input/feature-declaration checks |
| [Molecular solubility benchmark](https://github.com/TheThunda01/molecular-solubility-benchmark) | Implemented: attributed solubility data, descriptors, identity/scaffold grouping, training-only model selection, and held-out prediction/error checks |
| [Morphology transfer benchmark](https://github.com/TheThunda01/morphology-transfer-benchmark) | Implemented: raw LINCS profile subset, control normalization, explicit class-support exclusions, compound-held-out retrieval, and simple classification baselines |
| [Protein structure evidence](https://github.com/TheThunda01/protein-structure-evidence) | Implemented: carbonic anhydrase II residue mapping, structure superposition, separate confidence and displacement summaries, zinc-site geometry, and checked coordinate exports |
| [Yeast flux workbench](https://github.com/TheThunda01/yeast-flux-workbench) | Implemented: pinned Yeast-GEM model, six bound scenarios, selected flux variability, numerical diagnostics, and alternative-solver verification |

### Evidence and research workflows

| Project | Implemented scope |
| --- | --- |
| [EvidenceTrail](https://github.com/TheThunda01/evidencetrail) | Table checks, comparison coverage, missingness, review decisions, bounded archive verification, and optional comparison with a supplied expected digest |
| [Review Compass](https://github.com/TheThunda01/review-compass) | Review planning, literal keyword cues, query checks, exact-text search records, and explicit predecessor links for revisions |

### A visual introduction

| Project | Implemented scope |
| --- | --- |
| [Nature's Perfume Lab](https://github.com/TheThunda01/natures-perfume-lab) | Implemented: attributed terpene graphs, curated carbon correspondence, enzyme sequence comparison, structural coverage, and a reproducible molecular explorer |

## Later possibilities

These are options after the focused GFP and MAPK work, not completed experiments or scheduled commitments.

- **A public-health bridge:** extend Surveillance with a worked question about denominator changes and reporting revisions. Observed summaries can use the captured real snapshot; unavailable historical releases must remain unknown or be represented by explicitly synthetic scenarios.
- **Stronger external evaluation:** assess compatible independent conditions or data for the systems and morphology studies before changing model complexity. Consider a documented R/Bioconductor analysis, sequence-tool scaling, and an independent walkthrough of the review tools.
- **An experiment–model feedback loop:** develop a bounded question with suitable collaborators, a protocol, prospective measurements, and a validation plan. Current simulations and reanalyses do not supply that evidence.
- **Longer-term applications:** explore host–pathogen research, drug discovery, and literature-support tools only with suitable endpoints, data governance, and validation. Structure, solubility, or morphology scores alone cannot establish therapeutic benefit; the current collection is not a completed host–pathogen investigation or a validated autonomous research system.
- **Research-software contribution:** contribute a useful change to established software after reviewing its methods, contribution guidance, and tests.

A new repository should answer a question the existing projects cannot address. The [systems and cellular expansion](PROJECT_EXPANSION.md) preserves the scope of the earlier expansion; the [maintenance guide](MAINTENANCE.md) links review history and describes proposed manual upkeep.

## Evidence standard

Use original papers for study findings and official documentation for software behavior and dataset definitions. Keep project results separate from literature claims. Label synthetic examples and retrospective simulations, record source versions and reuse terms, and make failed checks understandable. A passing test does not establish biological correctness, clinical utility, or model generalization.

Document the input choices, assumptions, reasonable alternatives, and contributions to each extension. These practices are consistent with [Wilson et al. (2017), Good enough practices in scientific computing](https://doi.org/10.1371/journal.pcbi.1005510). AI assistance remains disclosed. The [shared standard](PORTFOLIO_STANDARDS.md), [assumption register](docs/assumptions.md), and [references](REFERENCES.md) provide the evidence framework.
