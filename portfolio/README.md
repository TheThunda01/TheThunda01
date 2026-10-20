# Computational biology portfolio

This collection brings together four small, runnable projects. Each one answers a different practical question: can we trust an input table, what do expression samples look like before inference, how should a model be evaluated, and what can sequence-file summaries actually tell us?

The aim is to make the reasoning easy to inspect. The projects include their own commands, tests, example results, methods, limitations, and data attribution. Two use real public data; two use explicitly synthetic fixtures. None claims a new biological discovery.

## Explore the projects

| Project | Data | What it demonstrates |
| --- | --- | --- |
| [Pasilla expression QC](pasilla-expression-qc/README.md) | Published Drosophila gene-count data | Matrix validation, sample metadata, normalization, PCA, and cautious interpretation |
| [Sequence Quality Toolkit](sequence-quality-toolkit/README.md) | Synthetic DNA strings | Python CLI design, FASTA parsing, manifest checks, explicit metric definitions |
| [Surveillance data quality](surveillance-data-quality/README.md) | Synthetic aggregate test reports | SQLite joins, missingness, denominator checks, reporting delay, and audit trails |
| [Cell-feature model validation](cell-feature-model-validation/README.md) | Public Wisconsin Diagnostic Breast Cancer benchmark | Training-only preprocessing and tuning, held-out evaluation, baseline comparison, and uncertainty limits |

Each directory is self-contained and prepared to become its own repository. This collection is the review copy. [The portfolio plan](PORTFOLIO_PLAN.md) explains how to develop it further; [publishing notes](PUBLISHING.md) explain the intended repository layout.

## How to review one

1. Read the question, data description, and limitations in its README.
2. Enter that project's directory and follow its environment instructions.
3. Run the tests and regenerate the example results.
4. Compare the output with the checked-in example, then inspect one method in the code.

The core tools are Python and SQLite. R/Bioconductor, distributed computing, and production deployment are future learning goals, not demonstrated capabilities of this release.

## Attribution and ownership

The initial implementation and documentation were developed with AI assistance and reviewed using executable examples and tests. Brandon should be able to explain and modify a project before presenting it as evidence of personal proficiency. Tests check software behavior; they do not certify scientific validity.

Original code is MIT-licensed within each project. Public datasets keep their own upstream licenses and citations. The Drosophila data and cell-feature benchmark were created by their credited research teams; they are not original data collected for this portfolio.
