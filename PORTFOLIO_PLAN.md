# Portfolio roadmap

The portfolio now has six connected projects. Its scope is careful computational work across biological data, statistical evaluation, and research-review software.

## Implemented work

| Project | Current evidence a reader can inspect |
| --- | --- |
| Pasilla expression QC | Public input fingerprints, validated metadata, normalization comparisons, sample distances, and leave-one-out PCA sensitivity |
| Sequence Quality Toolkit | Streaming FASTQ validation, per-cycle denominators, a provenance-checked public yeast prefix, FASTA/manifest reconciliation, and edge-case tests |
| Surveillance data quality | A real CDC snapshot, count and denominator checks, observation-window sensitivity, snapshot comparison, and synthetic as-of revision tests |
| Cell-feature model validation | Repeated nested CV, fold-level results, cross-fitted threshold development, calibration summaries, and preserved historical holdout results |
| EvidenceTrail | Table checks, reviewer pairing coverage, nonblank agreement, traceable review decisions, and Python/browser parity tests |
| Review Compass | Structured review planning, transparent literal keyword cues, field-completion summaries, export, and tested matching boundaries |

Background, rationale, and limitations are collected in the [project guide](PROJECT_GUIDE.md). The introductory GitHub tutorial repositories have been archived. The former portfolio-builder repository has been retained as Review Compass because it contains substantial project work; its history and template origin are preserved.

## Next development priorities

These are proposed learning milestones, not completed features or scheduled commitments.

1. Reproduce every example independently, explain the formulas and failure cases, and document a personal extension in each project.
2. Add a separate R/Bioconductor analysis to the expression project with a documented design, versioned environment, and careful treatment of library type. Keep exploratory QC separate from inferential claims.
3. Capture future surveillance releases prospectively. Only then use observed snapshots to study actual revisions and information availability over time.
4. Test sequence parsing and reporting on larger benign public files; measure runtime and peak memory before making scalability claims.
5. Extend model-evaluation work to a scientifically suitable independent dataset with a predeclared evaluation plan. Do not relabel a reused benchmark split as external validation.
6. Test the review tools with realistic, appropriately shareable workflows and record usability findings separately from methodological validity.
7. Make a small, useful contribution to an established research-software project after understanding its contribution and testing conventions.

## Evidence standard

Use original papers for study findings and official documentation for software behavior and dataset definitions. Keep calculated project results separate from literature claims. Label synthetic examples, record source versions and reuse terms, and make failed checks understandable. A passing test does not establish biological correctness or clinical utility.

For each project, be ready to explain why the data were chosen, what assumptions were made, what changed under a reasonable alternative, and which parts you personally reviewed and modified. These practices are consistent with Wilson et al. (2017), [Good enough practices in scientific computing](https://doi.org/10.1371/journal.pcbi.1005510), which motivates organization and reproducibility rather than any biological conclusion here.
