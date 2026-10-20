# A focused computational biology portfolio

The strongest story here is careful computational work that connects biology, data quality, and reproducible analysis. Breadth comes from making different kinds of decisions well, not from filling GitHub with overlapping tutorials.

## First release: four completed demonstrations

| Repository name | Main question | Evidence a reader can inspect |
| --- | --- | --- |
| `pasilla-expression-qc` | What should we check before interpreting a gene-count matrix? | Public input snapshot, file fingerprints, validated metadata, sample summaries, PCA comparisons, tests |
| `sequence-quality-toolkit` | Can a small sequence-file tool make its assumptions and failures clear? | Strict parser, synthetic edge cases, manifest reconciliation, defined GC/N50 calculations, reproducible reports |
| `surveillance-data-quality` | How do missing and invalid submissions change a summary? | Executed SQL, expected-report calendar, quarantined errors, matched denominators, test fixtures |
| `cell-feature-model-validation` | How do we evaluate a biological-feature classifier without leaking test information? | Training-only pipeline and model selection, baseline, held-out metrics, calibration bins, uncertainty caveats |

Use the existing [EvidenceTrail](https://github.com/TheThunda01/evidencetrail) project alongside these. It adds evidence-review workflow design to the portfolio without repeating the same analysis.

## Profile and presentation

Pin the four projects above and EvidenceTrail once the new repositories are published. Leave the remaining pin open until another substantial project is ready. Keep tutorial forks available, but do not present unmodified template code as a personal research result.

For each project, a reader should find the question, data source, executable command, example result, and limitations without searching through notebooks. The profile should describe these as educational analyses and software demonstrations. It should not claim a publication, clinical validation, independent discovery, or proficiency in a language that has not been used here.

## Next six to eight weeks

| Stage | Work | Ready when |
| --- | --- | --- |
| First week | Run all four projects independently; change one input, predict the effect, and explain the result | Brandon can explain each figure, denominator, test, and failure mode |
| Weeks 2–3 | Extend the Drosophila project with a separate R/Bioconductor analysis, using the original counts and a documented design | The R workflow runs in a pinned environment; sample type is considered; effect sizes and uncertainty are reported; conclusions stay within the design |
| Weeks 3–4 | Add a workflow runner to an existing project, with a small repeatable benchmark | A clean checkout rebuilds the expected outputs; the workflow provides useful dependency management rather than extra files alone |
| Weeks 5–6 | Reproduce one published result using data with clear reuse terms, preferably in a benign model-organism or public-health methods setting | The repository separates the published result, the reproduced result, and any unresolved discrepancy |
| Weeks 7–8 | Make a small, useful contribution to an established scientific software project | An issue or pull request explains a real problem, a focused change, and evidence that it works; acceptance is not promised |

These are suggested milestones, not a commitment or scheduled reminder. Scope should follow available time and genuine learning.

## Questions to answer before an interview

- Why were these data chosen, and what is outside their scope?
- Which decisions are defaults for a demonstration, and which follow from the study design?
- How would the result change if an input were missing, duplicated, mislabeled, or unusually large?
- What does a passing test tell us? What would still require scientific review?
- Which parts were AI-assisted, and what have you personally reviewed, changed, and understood?

## Evidence standard

Keep source claims close to their citations. Use original papers for study findings and official documentation for software behavior or data dictionaries. Label calculated project results as calculations, and keep simulated examples visibly separate from observations. A method reference does not validate this implementation.

Small reproducible projects, clear provenance, and useful documentation follow the practical recommendations in Wilson et al. (2017), *Good enough practices in scientific computing*, PLOS Computational Biology, [doi:10.1371/journal.pcbi.1005510](https://doi.org/10.1371/journal.pcbi.1005510). This paper motivates project organization; it is not evidence for any biological result in this collection.
