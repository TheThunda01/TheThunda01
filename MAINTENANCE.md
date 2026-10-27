# Keeping the projects useful

The portfolio is most useful when its examples remain runnable and its claims remain tied to the evidence. I would maintain it through small, reviewable updates rather than promise that every new method belongs in every repository.

## When a problem is reported

Capture the project revision, command, dependency versions, input schema, expected behavior, and actual behavior. Use a small shareable example where possible. Do not post confidential records or credentials in a public issue. Reproduce the problem before changing the analysis, add a regression check when it protects meaningful behavior, and document any effect on existing results.

## Before changing dependencies or data

Keep the previous reference outputs and source fingerprints. Rebuild in a clean environment, run the existing checks, and inspect differences in numerical results rather than assuming that a successful install proves equivalence. A source URL that now returns a different file is a new input revision, not a reason to silently replace the old checksum.

## A suggested review cadence

This is a proposed manual cadence, not an automatic service or a promise of scheduled work.

| Trigger | Work to do | Record to keep |
| --- | --- | --- |
| Before sharing or using a project | Run its quick start and tests; read the practical-use boundary | Revision, environment, outcome, unresolved issues |
| Monthly while actively developing | Triage reported problems and review the next improvement | Priority, acceptance criteria, owner if one is assigned |
| Quarterly, or when the scientific question changes | Rerun the saved literature queries, check important source updates and corrections, and assess whether they change a claim or method | Search date, exact query, retrieved records, screening decisions, change rationale |
| Before a proposed research pilot | Test representative inputs and an independent operator walkthrough; decide what would invalidate a result | Pilot scope, evidence, approval responsibilities, stop conditions |

## Updating a literature review

Preserve the earlier search record. Append a new dated run with the source, exact query, filters, sort order, page limits, returned identifiers, and screening rationale. Record an inaccessible paper as inaccessible; do not infer its findings from the title. Deduplicate publication identifiers when summarizing coverage, and keep supplementary software/documentation lookups separate from publication counts.

If a later result was used to choose a model or threshold, that result is now part of development. A fresh claim about generalization needs an appropriate new evaluation. If a paper changes the interpretation without requiring a code change, update the explanation and cite the reason.

The [project-specific practical-use guides](RESEARCH_REVIEW.md) contain the next improvements and acceptance criteria. They are a working backlog, not evidence that those improvements have been implemented.

## Historical portfolio branch

`portfolio/computational-biology-2026-10` preserves the early four-project layout. Those projects now have newer standalone repositories linked from the profile. Keep the branch as historical context; do not merge its older layout into the current profile. The current collection is defined by `portfolio.json`.

## Platform checks

Use a fresh Windows checkout as well as Linux CI when changing byte-level input checks or report writers. Files protected by a checksum need an explicit Git line-ending policy. Write generated text as UTF-8. Tests that specifically require symbolic links should report a clear capability skip when Windows cannot create them, while ordinary file-protection assertions still run. Keep a CI job that exercises the link-specific tests.


## Portfolio navigation

Keep the profile focused on the question, three featured studies, and the current investigation. The complete inventory belongs in [PROJECT_GUIDE.md](PROJECT_GUIDE.md); implemented scope and future work belong in [PORTFOLIO_PLAN.md](PORTFOLIO_PLAN.md). Keep those pages and the profile pins aligned when a project's role changes.

The featured reading path is Enzyme kinetics → GFP → MAPK. GFP is the current investigation; the reading order does not imply a data pipeline or a chronology of completed research. The six profile pins feature GFP, MAPK, Enzyme, Surveillance, EvidenceTrail, and Nature's Perfume Lab.

## Review records

These records describe their stated revisions and dates. They are historical evidence, not live status dashboards.

| Record | Scope |
| --- | --- |
| [Portfolio story, 27 October](docs/review-2026-10-27-story.md) | Profile hierarchy, complete project guide, roadmap, and project navigation |
| [Toolkit update, 27 October](docs/toolkit-strengthening-2026-10-27.md) | Model comparisons, interactive explorers, and editable workflows |
| [Maintenance review, 26 October](docs/review-2026-10-26.md) | Accuracy and reproducibility checks |
| [Writing review, 26 October](docs/writing-review-2026-10-26.md) | Editorial revisions based on Writing in the Sciences |
| [Scientific and editorial review, 21 October](docs/review-2026-10-21.md) | Dated scientific and documentation checks |
| [Earlier review, 20 October](docs/review-2026-10-20.md) | Earlier collection-wide review |
| [Research review](RESEARCH_REVIEW.md) and [verification update](VERIFICATION_REVIEW.md) | Original ten-project review history |
| [Systems and cellular expansion](PROJECT_EXPANSION.md) | Dated thirteen-project collection and three-project expansion |

The [references](REFERENCES.md), [source audit](docs/reference-audit.json), and [formula-rendering record](docs/math-rendering-checks.json) retain their detailed evidence and access limits.
