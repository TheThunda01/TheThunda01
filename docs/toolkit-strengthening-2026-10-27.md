# Inspectable models, results and workflows

This 27 October 2026 update adds reproducible inspection tools to all fourteen projects. The links below point to the exact reviewed commits. Each change has a linked pull request whose page records its current review and merge status.

## Choose a question to inspect

| Project guide | Tool | What becomes easier to inspect | Change |
| --- | --- | --- | --- |
| [Nature's Perfume Lab](https://github.com/TheThunda01/natures-perfume-lab/blob/21e3035cccb9fe866c92605d6c1fb97ef8c14f0f/docs/molecular-inspection.md) | Avogadro / RDKit | Inspect the three attributed structures with carbon maps and stereochemistry preserved. | [Review](https://github.com/TheThunda01/natures-perfume-lab/pull/1) |
| [Protein structure evidence](https://github.com/TheThunda01/protein-structure-evidence/blob/eb01914b9994e15a0389c135ab413c21b802ff72/docs/chimerax-inspection.md) | ChimeraX | View the verified saved overlay without a second fit; reproduce a native session. | [Review](https://github.com/TheThunda01/protein-structure-evidence/pull/2) |
| [Molecular solubility benchmark](https://github.com/TheThunda01/molecular-solubility-benchmark/blob/704d4122ef44f2521459002c7b9a38ef0c589c58/docs/prediction-inspection.md) | Plotly | Trace frozen prediction errors to source rows on common axes. | [Review](https://github.com/TheThunda01/molecular-solubility-benchmark/pull/2) |
| [MAPK dynamics lab](https://github.com/TheThunda01/mapk-dynamics-lab/blob/c06f750a448034feb5d5be92bc978d4b4364944b/docs/copasi-comparison.md) | COPASI | Compare 648 baseline concentrations against an independent numerical implementation. | [Review](https://github.com/TheThunda01/mapk-dynamics-lab/pull/2) |
| [Enzyme kinetics workbench](https://github.com/TheThunda01/enzyme-kinetics-workbench/blob/e8312047a4f7b489712869a7fdd0c4d0578a596e/docs/profile-explorer.md) | Plotly | Connect 964 checked parameter-profile points with their predicted curves. | [Review](https://github.com/TheThunda01/enzyme-kinetics-workbench/pull/2) |
| [Yeast flux workbench](https://github.com/TheThunda01/yeast-flux-workbench/blob/3f2618468b283a49bddcaceccba7fc38035053b6/docs/cytoscape-inspection.md) | Cytoscape | Inspect a verified 52-node, 54-edge neighborhood with explicit unavailable FVA states. | [Review](https://github.com/TheThunda01/yeast-flux-workbench/pull/2) |
| [GFP active learning](https://github.com/TheThunda01/gfp-active-learning/blob/520b812585874930fb5608b78c24e6e3c3532f2a/docs/seed-explorer.md) | Plotly | Compare paired acquisition seeds while keeping the original experiment separate from the ablation. | [Review](https://github.com/TheThunda01/gfp-active-learning/pull/2) |
| [Morphology transfer benchmark](https://github.com/TheThunda01/morphology-transfer-benchmark/blob/f1bcb0fab3f16939a5f32f80e850fc48c3f44b82/docs/query-explorer.md) | Plotly | Compare query retrieval with its own gallery expectation and denominators. | [Review](https://github.com/TheThunda01/morphology-transfer-benchmark/pull/2) |
| [Pasilla expression QC](https://github.com/TheThunda01/pasilla-expression-qc/blob/1f58f45219dfae31b0e99fe6940914e914fba344/docs/sample-explorer.md) | Plotly | Link sample labels, normalization, PCA and omission sensitivity. | [Review](https://github.com/TheThunda01/pasilla-expression-qc/pull/2) |
| [Cell-feature model validation](https://github.com/TheThunda01/cell-feature-model-validation/blob/fbe33966c950a75008cde70a5cf1ba6b47de06c5/docs/data-roles-diagram.md) | draw.io / Inkscape | Follow distinct data roles in assessment, threshold tuning, refitting and holdout inspection. | [Review](https://github.com/TheThunda01/cell-feature-model-validation/pull/2) |
| [Sequence Quality Toolkit](https://github.com/TheThunda01/sequence-quality-toolkit/blob/0211b982f9c99b53524a4e7df7870e2f4e38d361/docs/quality-visualization.md) | Matplotlib | Read per-cycle quality beside the number of reads contributing to each mean. | [Review](https://github.com/TheThunda01/sequence-quality-toolkit/pull/3) |
| [Surveillance data quality](https://github.com/TheThunda01/surveillance-data-quality/blob/2298ecc0c1846a318e51c717a16e3cccc0ec58fc/docs/denominator-visualization.md) | Matplotlib | Inspect test counts and window sensitivity while preserving missing versus zero states. | [Review](https://github.com/TheThunda01/surveillance-data-quality/pull/3) |
| [EvidenceTrail](https://github.com/TheThunda01/evidencetrail/blob/3db18aeb89f37354263d0c05ea8acb03a6e04163/docs/reviewer-workflow.md) | draw.io | Distinguish pairing coverage, answer agreement, locator differences and human decisions. | [Review](https://github.com/TheThunda01/evidencetrail/pull/2) |
| [Review Compass](https://github.com/TheThunda01/review-compass/blob/3d40c5863ba52fb0a9be07d75028476171890bef/docs/search-workflow.md) | draw.io | Follow the handoff from planning to database execution and operator-reported records. | [Review](https://github.com/TheThunda01/review-compass/pull/3) |

## Reproduce an artifact

Open the project's linked guide and use its pinned analysis environment first. Each guide identifies the required source files, optional viewer or plotting dependencies, export command, generated artifacts and limitations. Keep editable models and diagrams with their scripts and provenance. Separate visualization requirements preserve the core analysis environment.

The Plotly explorers run offline once their HTML has been generated. Download the HTML from its linked commit and open it locally; GitHub's file viewer displays source rather than the interactive page. Static previews remain available for readers who do not launch a viewer. The molecular-solubility explorer is generated locally from its verified bundle rather than committing another large HTML file.

## What was checked

Core test suites and the documented numerical reproductions were run in project-specific environments. Review also covered source identities, units, missing-data states, editable diagram layouts, browser interactions and native viewer imports. The MAPK baseline was compared with COPASI; the yeast network's original attributes were read back from Cytoscape. Pull-request checks record hosted validation of each published commit. Native desktop checks are documented in the linked project guides and do not run in hosted CI.

The original source snapshots and historical numerical results are preserved. Windows checkout fixes prevent newline conversion from breaking exact-byte fingerprints. Tests and viewer agreement establish the listed software behavior and artifact fidelity; they do not establish biological correctness, generalization, experimental validity or calibrated uncertainty.

## Scope of the tools

These additions make existing work easier to interrogate and reproduce. They are not a new independent experiment or the author's personal-explanation checkpoint. AI assistance is disclosed in the repositories and pull requests.

Blender and Fiji remain available for work that supplies an appropriate 3D or image-analysis question and source material. This update does not add decorative 3D scenes or claim raw-image analysis for a repository that uses image-derived tables. JupyterLab remains available for exploration; the reproducible additions here use scripts and saved artifacts.
