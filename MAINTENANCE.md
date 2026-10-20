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
