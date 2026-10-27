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

The practical-use guide describes an input/output contract, a worked use case, checks before relying on a result, known limits, and prioritized improvements with acceptance criteria. Each literature review records its question, search strategy, evidence, implementation consequences, remaining work, and review limitations. `docs/search-log.json` preserves the search metadata and screening decisions in a machine-readable form. Each project also links a glossary, assumption register, reference audit, and dated correction record from its README.

## Connecting each project to the portfolio

Use a short paragraph in “Why this project” to explain the project's role in [From biological measurements to better experiments](PROJECT_GUIDE.md). The project-context guide can give a related next stop. Keep the seven README sections above, and preserve the result, provenance, and material limitations beside the relevant claims.

The featured reading path is Enzyme kinetics, GFP, then MAPK. Supporting projects contribute measurement checks, model evaluation, evidence workflows, or an accessible visual introduction. A conceptual connection must not imply that separate datasets or tools already form an integrated workflow. Keep current investigations distinct from proposed extensions, and link dated maintenance records without making them the main reading path.

## Evidence and language

Scientific statements should point to an appropriate source. A method paper can explain an algorithm; it cannot validate this implementation. An official data dictionary can define a field; it cannot establish that a particular extract is complete. A software test can check an invariant; it cannot establish biological meaning. The distinction should be visible where a reader needs it, without repeating the same disclaimer after every sentence.

Write plainly and explain the biological or statistical reason for a choice. Prefer an observable statement such as “the parser rejects duplicate sample IDs” over a broad label such as “production ready.” Keep exploratory findings, predictions, and experimentally established results separate.

Define specialist terms and abbreviations at their first meaningful use, then provide a project-specific glossary for reference. An assumption register explains each material choice, its evidence or practical rationale, checks performed, and the consequences if it fails. A computational convenience should not acquire a biological justification just because it makes an example easier to run.

Use descriptive author–year citations. Give papers a verified title, author or first author with “et al.”, year, journal, volume, issue where available, pages or article number, and DOI/PMID where verified. Give datasets and software their organization, version or commit, canonical link, access date, and separate reuse terms. Record source access honestly: reading an abstract is not a full-text appraisal. The reference audit links each source to supported claims, corrections, and limits. Historical search records and frozen outputs retain their original context; current guidance explains later corrections.

This approach draws on [Wilson et al. (2017)](https://pubmed.ncbi.nlm.nih.gov/28640806/) for reproducible research organization and [Barker et al. (2022)](https://pubmed.ncbi.nlm.nih.gov/36241754/) for software metadata and reuse. The CODE roadmap of [Di Cosmo et al. (2026)](https://doi.org/10.1038/s41597-026-06705-6) organizes recommendations around Open, Document, Execute, and Collaborate. These are practice frameworks, not evidence that these projects have met an external certification standard. See the [complete references](REFERENCES.md).

## Writing for readers

The writing approach draws on *Writing in the Sciences*, Units 1–7, supplied for this editorial review. Apply their principles to the reader's task:

- Lead each paragraph with its main point, then give the evidence or explanation. Separate a result from its interpretation and limits.
- Name the actor when it helps: the script checks inputs, the model predicts a value, or the reviewer records a decision. Use precise verbs and keep the subject close to its verb.
- Cut repetition, empty qualifiers, and unnecessary jargon. Define technical terms where readers first need them, and use parallel wording for comparable methods or options.
- Explain metrics, units, denominators, and uncertainty beside the results. Summarize the pattern without repeating every table entry.
- Preserve the strength of the evidence. Editing must not turn association into causation, an exploratory result into validation, or a future goal into an accomplishment. Retain source attribution and AI-assistance disclosure.

These principles guide revision, not a word-count target or a ban on passive voice. Keep procedural detail needed to reproduce the work. The [writing review](docs/writing-review-2026-10-26.md) records how they were applied to the current documentation.

## Moving toward professional use

The current projects are research demonstrations with explicit checks and limitations. Moving a project into a team workflow requires a defined use case, representative input data, an independent run, agreement about failure handling, and a named person responsible for interpreting the result. Operational use also needs suitable privacy, access, retention, maintenance, and support arrangements for that setting. Those arrangements are not supplied by a GitHub repository.

A proposed extension should state what changes, why it matters, and how success will be assessed. Useful acceptance criteria include a failing example that the change fixes, a reproducible comparison on appropriate data, an interoperable file that another tool can read, or a documented operator walkthrough. Test counts alone are not acceptance criteria for a scientific claim.

## Checking consistency

After cloning the project repositories listed in `portfolio.json` into one directory, run:

```bash
python scripts/check_portfolio_docs.py --root /path/to/cloned-repositories
```

The script checks the common README structure, the required practical-use and review sections, search-log metadata, and relative links in those pages. It does not assess the completeness of a search, the quality of a paper, or the truth of a scientific claim. See the [review record](RESEARCH_REVIEW.md) and [maintenance guide](MAINTENANCE.md) for those human review tasks.

Numbered updates preserve earlier search records. The checker validates `docs/search-update-*.json` when present. `--require-update 02` requires that particular update in every repository named in the selected manifest; use `--manifest portfolio-round2.json` for the original ten-project second pass. The later projects have their own initial searches. Duplicate JSON keys fail rather than silently replacing an earlier value.

For the current scientific and editorial review, add `--editorial-review 2026-10-21`. The earlier `2026-10-20` records remain available. This checks review-file presence, source-audit fields, and local links in authored documentation. It cannot establish that every term is understandable, every assumption has been found, or a citation supports its claim; those require reading and judgment.

## Formula rendering

Use GitHub's protected inline math delimiters and fenced `math` blocks so Markdown does not remove LaTeX escapes or equation line breaks. Check the actual rendered page for errors; balanced delimiters alone are not enough. Keep commands and field identifiers as code. Preserve audit-critical historical protocol text, with an equivalent rendered explanation in its current guide when needed. Report generators should emit the same math formatting as committed reports, and artifact records must reflect any presentation-only byte changes.

The [formula rendering check](docs/math-rendering-checks.json) records the pages and expression counts verified in the browser.
