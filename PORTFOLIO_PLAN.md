# Portfolio roadmap

This ten-project collection connects molecular modeling with the data, statistics, software, and evidence practices that support it. My interests include AI, mathematical modeling, protein structure and function, enzyme activity, pathways and interactions, drug discovery and repurposing, host–pathogen biology, and evidence-aware scientific reasoning. The projects develop parts of that foundation; they do not establish expertise across all these areas.

**Portfolio link for a résumé or CV: [github.com/TheThunda01](https://github.com/TheThunda01).** The [project guide](PROJECT_GUIDE.md) explains the rationale, concepts, and limitations of each project.

The [20 October practical-use review](RESEARCH_REVIEW.md) records the current evidence review and implementation changes. Project-specific guides now keep the next improvements alongside explicit acceptance criteria. The [maintenance guide](MAINTENANCE.md) describes a proposed review cadence; ongoing updates are not scheduled automatically.

## Implemented foundation projects

| Project | Current evidence a reader can inspect |
| --- | --- |
| Pasilla expression QC | Public input fingerprints, normalization and PCA sensitivity, condition/read-type design diagnostics, and an explicit unresolved source-label caveat |
| Sequence Quality Toolkit | Streaming FASTQ validation, paired-file consistency, per-cycle denominators, a provenance-checked public yeast prefix, and FASTA/manifest reconciliation |
| Surveillance data quality | A real CDC snapshot, denominator-change diagnostics, observation-window sensitivity, snapshot comparison, and synthetic as-of revision tests |
| Cell-feature model validation | Repeated nested CV, calibration, cross-fitted thresholds, conditional prevalence scenarios, and preserved historical holdout results |
| EvidenceTrail | Table checks, reviewer comparisons, downloadable field/locator completeness, traceable review decisions, and Python/browser parity tests |
| Review Compass | Structured planning, transparent keyword cues, exact-query structural checks with fingerprints, export, and tested matching boundaries |

## Implemented molecular projects

These repositories include runnable analyses, pinned public inputs, worked results, explanatory guides, and automated checks. Their methods are distinct from the future research goals below; software review and reproducibility checks do not establish prospective biological validation.

| Project | Implementation scope |
| --- | --- |
| Enzyme kinetics workbench | Archived Puromycin data, Michaelis–Menten fits, apparent-parameter profiles, concentration-range sensitivity, and conditional mathematical information scenarios |
| Protein structure evidence | Carbonic anhydrase II residue mapping, experimental/predicted structure superposition, confidence and displacement summaries, and zinc-site geometry |
| GFP active learning | A provenance-documented GFP fluorescence subset, retrospective acquisition-policy comparisons, fixed labeling budgets, and a separate sequence-shifted evaluation subset |
| Molecular solubility benchmark | Attributed solubility data, RDKit descriptors, identity/scaffold grouping, training-only model selection, and held-out error/distance diagnostics |

All ten projects use public or clearly labeled synthetic data. The molecular projects do not conduct laboratory experiments, synthesize molecules, establish new mechanisms, or validate a drug candidate.

## Next learning and research goals

These are proposed milestones, not implemented features or scheduled commitments.

1. Reproduce each example independently, explain the mathematics and failure cases, and document a personal extension. Strengthen programming, algorithms, linear algebra, calculus, probability, statistics, and machine learning alongside domain knowledge.
2. Extend molecular modeling only when the biological question and measurements justify it. Compare mechanistic and statistical models, examine identifiability, and distinguish predictions from causal explanations.
3. Explore an experiment–model feedback loop with suitable collaborators and a defined system. Any future laboratory work would require an actual protocol, appropriate resources, prospective measurements, and independent validation. The current retrospective simulations are preparation for this goal.
4. Build a separate pathway or molecular-interaction project around a focused, well-documented public dataset. Pathway annotation and network proximity alone should not be presented as causal mechanisms.
5. Study drug-discovery and repurposing methods with clearly defined endpoints and appropriate validation. Structure or solubility scores alone cannot establish binding, efficacy, safety, or clinical benefit.
6. Develop host–pathogen research questions with domain collaborators, using appropriate data governance and a clearly bounded biological question. None of the four new molecular examples represents a host–pathogen study.
7. Explore LLMs or agents for literature organization, scientific reasoning support, and research planning with traceable sources and human review. EvidenceTrail and Review Compass are current foundations for these ideas; they are not validated autonomous scientific agents.
8. Deepen the foundation projects: add a documented R/Bioconductor analysis, capture future surveillance releases prospectively, measure sequence-tool scaling, evaluate on suitable independent data, and study realistic review-tool usability.
9. Contribute a small, useful change to established research software after understanding its methods, contribution guidelines, and tests.

## Evidence standard

Use original papers for study findings and official documentation for software behavior and dataset definitions. Keep calculated project results separate from literature claims. Label synthetic examples and retrospective simulations, record source versions and reuse terms, and make failed checks understandable. A passing test does not establish biological correctness, clinical utility, or model generalization.

For each project, be ready to explain why the data were chosen, what assumptions were made, what changed under a reasonable alternative, and which parts you personally reviewed and modified. These practices are consistent with Wilson et al. (2017), [Good enough practices in scientific computing](https://doi.org/10.1371/journal.pcbi.1005510), which motivates organization and reproducibility rather than any biological conclusion here. AI assistance is disclosed; understanding and responsibility cannot be delegated to a tool.
