# A second pass: making results easier to verify

The first practical-use review added handoff checks and explicit input contracts. This second pass, also on **20 October 2026**, follows the next items in those project backlogs: inspect the underlying numbers, verify exported artifacts, and preserve the records behind a workflow. It is a different review scope on the same day, not evidence of ongoing monitoring.

The [starting revisions](docs/review-baseline-02.json) preserve the boundary between the two passes. Earlier search records remain available. Each project's new `docs/search-update-02.json` records its narrower follow-up queries, selection decisions, supplementary sources and access limits.

All ten projects received an implementation update. The original scientific data and result files were preserved; new verification examples are stored separately. The common documentation structure remains the same.

## Why these changes

A file can match a checksum while still contain an incorrect calculation. A model score can be reproducible while still be inappropriate for a new dataset. An explicit distinction between those questions makes a small research tool easier to evaluate.

The current [TOP guideline update](https://pubmed.ncbi.nlm.nih.gov/42557573/) separates transparent research practices from computational reproducibility and other verification activities. That distinction informs the way these projects describe their checks; it does not certify them. A [scientific-software engineering tutorial](https://pubmed.ncbi.nlm.nih.gov/41186375/) and the [HORTON software case study](https://pubmed.ncbi.nlm.nih.gov/38651814/) provide practical context for testing, documentation and maintainability. Those two papers were appraised from abstracts in this update, so they support broad practice choices rather than a detailed comparison of implementations.

The [portfolio-level search update](docs/standards-search-update-02.json) retrieved all 11 results of its narrow PubMed query across two pages. Three directly relevant sources were retained. This is a focused evidence update, not an exhaustive systematic review. The TOP body was only partly retrieved; the record states which material was inspected.

## How to read the verification outputs

| Project | Verification-focused improvement | Boundary to keep in mind |
| --- | --- | --- |
| Enzyme kinetics workbench | Compare stored fits with an analytic maximum-rate calculation and a separate scalar search | Same least-squares objective; agreement does not establish the biological model |
| GFP active learning | Export final-budget predictions and recompute their evaluation metrics from source labels | Covers the final budget, not every learning-curve point or prospective performance |
| Protein structure evidence | Verify the aligned model, transform and receipt against pinned source data | Geometric/file consistency, not authenticated authorship or protein function |
| Molecular solubility benchmark | Export held-out predictions using frozen model choices and reconstruct the reported metrics | Uses observed benchmark partitions; no new independent validation claim |
| Pasilla expression QC | Compare numeric result tables with declared tolerances and exact sample identities | A comparison to a chosen reference cannot resolve the source-label discrepancy |
| Sequence Quality Toolkit | Require an optional input lock before publishing QC outputs | Matching bytes do not establish sample identity or downstream suitability |
| Surveillance data quality | Return versioned, machine-readable preflight diagnostic codes | A valid snapshot contract does not establish population coverage |
| Cell-feature model validation | Record and check explicit feature-mapping declarations | Completeness of a declaration is not proof of measurement equivalence |
| EvidenceTrail | Compare an audit archive with an independently supplied expected digest | Trust comes from how the reference digest was obtained, not from the hash alone |
| Review Compass | Link a new search-record revision to its predecessor and record why it changed | A recorded lineage cannot prove that every search or revision was disclosed |

Each tool reports the specific claim it checked. Matching a reference digest means the bytes match that reference. Recomputing a metric checks the relation between saved predictions, labels and the metric definition. Neither proves that the inputs are scientifically suitable, that a model generalizes, or that a workflow is ready for consequential use.

The project-specific practical-use guides explain commands, failure behavior and remaining acceptance criteria. For work with a research team, the next step is still a scoped pilot using representative data and an independent operator. A successful pilot needs to record unexpected inputs, ambiguous interpretations and what the team will do when a check fails.

## Documentation checks

The [shared checker](scripts/check_portfolio_docs.py) now also validates any numbered search-update records and rejects duplicate JSON keys. To require the second update in every local checkout:

```bash
python scripts/check_portfolio_docs.py --root /path/to/cloned-repositories --require-update 02
```

It checks document structure and machine-readable records. It does not establish that a search is complete or that a source supports every claim. Those remain review tasks.
