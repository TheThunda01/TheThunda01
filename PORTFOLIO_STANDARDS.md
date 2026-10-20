# A shared standard for the portfolio

I want each project to be useful to someone who did not watch it being built. A reader should be able to understand the question, run a small example, trace the inputs, and see where the answer stops being reliable. Consistent documentation helps with that; identical scientific claims would not.

## A familiar route through each project

Every project README follows the same sequence:

1. **Why this project** — the problem, intended reader, and rationale.
2. **What it does** — implemented behavior, with a clear boundary around future ideas.
3. **Quick start** — dependencies, commands, and expected files.
4. **Example results** — inspectable outputs and their interpretation.
5. **Practical use and limitations** — where the tool fits and what an operator still needs to check.
6. **Documentation** — links to the context, biology or concepts, methods, sources, practical-use guide, and literature review.
7. **Development and reuse** — tests, contribution guidance, and separate code/data terms where needed.

The practical-use guide describes an input/output contract, a worked use case, checks before relying on a result, known limits, and prioritized improvements with acceptance criteria. Each literature review records its question, search strategy, evidence, implementation consequences, remaining work, and review limitations. `docs/search-log.json` preserves the search metadata and screening decisions in a machine-readable form.

## Evidence and language

Scientific statements should point to an appropriate source. A method paper can explain an algorithm; it cannot validate this implementation. An official data dictionary can define a field; it cannot establish that a particular extract is complete. A software test can check an invariant; it cannot establish biological meaning. The distinction should be visible where a reader needs it, without repeating the same disclaimer after every sentence.

Write plainly and explain the biological or statistical reason for a choice. Prefer an observable statement such as “the parser rejects duplicate sample IDs” over a broad label such as “production ready.” Keep exploratory findings, predictions, and experimentally established results separate.

This approach draws on [Wilson et al. (2017)](https://pubmed.ncbi.nlm.nih.gov/28640806/) for reproducible research organization and [Barker et al. (2022)](https://pubmed.ncbi.nlm.nih.gov/36241754/) for software metadata and reuse. The [CODE roadmap (2026)](https://doi.org/10.1038/s41597-026-06705-6) adds a useful emphasis on execution, documentation, and collaboration. These are practice frameworks, not evidence that these projects have met an external certification standard.

## Moving toward professional use

The current projects are research demonstrations with explicit checks and limitations. Moving a project into a team workflow requires a defined use case, representative input data, an independent run, agreement about failure handling, and a named person responsible for interpreting the result. Operational use also needs suitable privacy, access, retention, maintenance, and support arrangements for that setting. Those arrangements are not supplied by a GitHub repository.

A proposed extension should state what changes, why it matters, and how success will be assessed. Useful acceptance criteria include a failing example that the change fixes, a reproducible comparison on appropriate data, an interoperable file that another tool can read, or a documented operator walkthrough. Test counts alone are not acceptance criteria for a scientific claim.

## Checking consistency

After cloning the ten repositories into one directory, run:

```bash
python scripts/check_portfolio_docs.py --root /path/to/cloned-repositories
```

The script checks the common README structure, the required practical-use and review sections, search-log metadata, and relative links in those pages. It does not assess the completeness of a search, the quality of a paper, or the truth of a scientific claim. See the [review record](RESEARCH_REVIEW.md) and [maintenance guide](MAINTENANCE.md) for those human review tasks.
