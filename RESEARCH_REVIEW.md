# Research and practical-use review

**Reviewed: 20 October 2026.** This review asks how the ten projects can become more useful in research workflows without claiming that a working example is already a deployed professional service.

The [baseline revision record](docs/review-baseline.json) identifies the starting commit of each repository. It makes the review's scope explicit even after later updates change the default branch.

A [second verification-focused pass](VERIFICATION_REVIEW.md) on the same date follows the next practical priorities while preserving this first review and its search records.

## How the evidence was gathered

Each repository has a focused question, a dated `docs/search-log.json`, and a readable `docs/literature-review.md`. Publication discovery starts with PubMed, then uses primary publisher pages, official dataset and software documentation, and selected related repositories. Recent methodological work is considered alongside the original data and foundational methods. Search records distinguish total hits, retrieved records, screened records, cited evidence, and sources inspected only through an abstract.

This is a structured rapid review supporting software development. It is not an exhaustive systematic review or a meta-analysis. Queries are focused, some result sets are screened through a bounded page, and subscription databases are not searched. A missing result is not evidence that a method has no literature. No protocol was registered and no independent pair of human reviewers screened the evidence. These limits belong in the record so another reader can decide whether the search is adequate for their question.

The search-record format draws on PRISMA-S, the literature-search extension to Preferred Reporting Items for Systematic Reviews and Meta-Analyses, described by [Rethlefsen et al. (2021)](https://pubmed.ncbi.nlm.nih.gov/33499930/): identify the source, preserve the executed query and limits, record dates, and explain record handling. It does not imply PRISMA compliance. The separate [standards search log](docs/standards-search-log.json) records the cross-portfolio guidance search, including zero-result title queries, supplemental lookups, and duplicate publications. Full citation details are in [References](REFERENCES.md).

## What changes as a result

The completed changes below target handoff reliability, inspectable assumptions, and useful integration points. The source-to-claim tables explain why each change is useful and what the cited evidence cannot establish. Each practical-use guide ends with a prioritized backlog and acceptance criteria.

| Project | Implemented improvement | Evidence and practical use |
| --- | --- | --- |
| Enzyme kinetics workbench | Omit whole concentration levels and inspect parameter shifts and extrapolation | [Review](https://github.com/TheThunda01/enzyme-kinetics-workbench/blob/main/docs/literature-review.md) · [Guide](https://github.com/TheThunda01/enzyme-kinetics-workbench/blob/main/docs/practical-use.md) |
| Protein structure evidence | Export aligned coordinates with an explicit transform and provenance receipt | [Review](https://github.com/TheThunda01/protein-structure-evidence/blob/main/docs/literature-review.md) · [Guide](https://github.com/TheThunda01/protein-structure-evidence/blob/main/docs/practical-use.md) |
| GFP active learning | Audit saved query histories, identities, budgets, paired starts, and summaries | [Review](https://github.com/TheThunda01/gfp-active-learning/blob/main/docs/literature-review.md) · [Guide](https://github.com/TheThunda01/gfp-active-learning/blob/main/docs/practical-use.md) |
| Molecular solubility benchmark | Export and inspect outer/inner split membership without fitting a model | [Review](https://github.com/TheThunda01/molecular-solubility-benchmark/blob/main/docs/literature-review.md) · [Guide](https://github.com/TheThunda01/molecular-solubility-benchmark/blob/main/docs/practical-use.md) |
| Pasilla expression QC | Verify a result package's expected files, input fingerprints, and sample labels | [Review](https://github.com/TheThunda01/pasilla-expression-qc/blob/main/docs/literature-review.md) · [Guide](https://github.com/TheThunda01/pasilla-expression-qc/blob/main/docs/practical-use.md) |
| Sequence Quality Toolkit | Create and verify a byte-level input lock before running sequence checks | [Review](https://github.com/TheThunda01/sequence-quality-toolkit/blob/main/docs/literature-review.md) · [Guide](https://github.com/TheThunda01/sequence-quality-toolkit/blob/main/docs/practical-use.md) |
| Surveillance data quality | Validate snapshot identity, source metadata, timestamps, fingerprints, and schema | [Review](https://github.com/TheThunda01/surveillance-data-quality/blob/main/docs/literature-review.md) · [Guide](https://github.com/TheThunda01/surveillance-data-quality/blob/main/docs/practical-use.md) |
| Cell-feature model validation | Check candidate-file schema, provenance declarations, and exact benchmark overlap | [Review](https://github.com/TheThunda01/cell-feature-model-validation/blob/main/docs/literature-review.md) · [Guide](https://github.com/TheThunda01/cell-feature-model-validation/blob/main/docs/practical-use.md) |
| EvidenceTrail | Verify a bounded audit bundle against its manifest without extracting it | [Review](https://github.com/TheThunda01/evidencetrail/blob/main/docs/literature-review.md) · [Guide](https://github.com/TheThunda01/evidencetrail/blob/main/docs/practical-use.md) |
| Review Compass | Export exact-query search records with declared context and explicit draft/executed status | [Review](https://github.com/TheThunda01/review-compass/blob/main/docs/literature-review.md) · [Guide](https://github.com/TheThunda01/review-compass/blob/main/docs/practical-use.md) |

## Verification and next decisions

The original scientific input and result files were preserved. New commands have positive examples and failure-case tests; a separate AI-assisted review also checked the claims against what the code actually verifies. That review found and corrected an impossible surveillance release/capture chronology and malformed CSV quoting in the cell-data preflight.

At the end of this first pass, priorities included per-observation prediction exports and explicit feature-mapping records. The [second pass](VERIFICATION_REVIEW.md) implements those bounded checks. Independent viewer round trips remain necessary before claiming tested viewer compatibility, and a suitable independent cohort remains necessary for external model validation. A checksum manifest helps detect accidental changes but does not establish authenticity when a file and its manifest are both replaced.

The [documentation checker](scripts/check_portfolio_docs.py) verifies the common section order, required review metadata, and inline relative links across local checkouts. It is a consistency check, not a score for methodological quality.

## What practical use still requires

The common next step is a well-defined pilot: representative inputs, an independent operator, an expected output or failure condition, and a record of problems. Biological interpretation and consequential decisions need domain review and evidence appropriate to the intended setting. The projects' small public examples do not provide that evidence on their own.

The [shared standard](PORTFOLIO_STANDARDS.md) defines documentation and review expectations. The [maintenance guide](MAINTENANCE.md) describes how to update dependencies, data, and literature records without silently changing the analysis history. Each practical-use guide has its own prioritized next steps and acceptance criteria.
