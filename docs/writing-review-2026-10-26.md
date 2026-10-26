# Writing review: applying *Writing in the Sciences*

Review date: **26 October 2026**.

This editorial pass applies the seven supplied *Writing in the Sciences* guides to the profile and all thirteen projects. It builds on the [maintenance review](review-2026-10-26.md). The aim is to help readers find the question, understand the method, and interpret the result without losing the qualifications that make a scientific claim accurate.

## Principles applied

| Guide | Application to the portfolio |
| --- | --- |
| Unit 1: effective writing | Cut empty qualifiers, repeated ideas, and unnecessary jargon. Keep words that define the scope or uncertainty of a claim. |
| Unit 2: verbs | Use concrete verbs and name the actor when known: a script validates inputs, a model predicts, or a reviewer records a decision. Keep subjects close to their verbs. |
| Unit 3: sentences and paragraphs | Give each paragraph one purpose, lead with its main point, and use parallel wording for comparable methods and options. |
| Unit 4: the writing process | Organize ideas before polishing sentences, then review the changes for meaning and consistency. |
| Unit 5: scientific papers | Separate observations from interpretation, explain metrics near the results, retain negative findings, and preserve reproducibility details. |
| Unit 6: publication and review | Preserve attribution and AI-assistance disclosure; check that clearer wording does not overstate the evidence. |
| Unit 7: other scientific writing | Ground the profile in a concrete project, distinguish implemented work from future aims, and keep bounded literature reviews distinct from systematic reviews. |

The guides were supplied as seven PDFs for this review. They are not redistributed here. Their manuscript advice is adapted to GitHub documentation: software behavior remains in the present tense, README sections retain their purpose, and passive voice remains where it makes the action clearer. The [shared standard](../PORTFOLIO_STANDARDS.md#writing-for-readers) records these principles for future edits.

## What changed

The profile now introduces the work directly and uses the GFP comparison as a concrete example. Project summaries describe actions instead of listing keywords. The project guide separates methods from their limits, and the roadmap leads with the existing GFP and MAPK learning priorities.

Across all thirteen projects, revisions focus on the README, project context, biology or concepts, and practical-use guide. Methods guides were also revised where clearer actors or paragraph boundaries helped. Definitions and assumptions were reviewed without forcing changes to concise passages. Dated reviews, search records, frozen protocols, source bibliographies, and generated reports retain their historical wording.

Examples of the approach:

| Before | After | Purpose |
| --- | --- | --- |
| “EvidenceTrail provides deterministic table checks…” | “EvidenceTrail applies fixed rules to extraction tables…” | Replace an abstract noun phrase with a concrete action. |
| “A curved relationship between substrate concentration and reaction rate can be summarized by a simple model, but a plausible curve does not mean every parameter is well determined.” | “A model can fit reaction rates well while leaving its parameters uncertain.” | Lead with the scientific point and remove repetition. |
| “Its new standalone recorder helps keep the text of a search with the context reported by the person who ran it.” | “The standalone recorder stores the exact search text with the context you report.” | Name the action and retain the operator-reported scope. |

Some revisions add a short definition or split a dense paragraph rather than reduce the word count. The test is whether readers can follow the argument, not whether every passage is shorter.

## Checks and limits

The changes affect narrative Markdown only. Commands, equations, code, data, numerical results, citations, licenses, and historical records remain unchanged. Documentation checks cover required sections and local links; a separate audit checks links between the project repositories. Comparisons against the preceding revisions check command blocks, mathematical expressions, identifiers, numbers, and citation destinations. Reviewers also examine the prose for changes in meaning that a token comparison cannot detect.

The pass revised 65 existing Markdown files and added this review. The shared documentation checker passed for all thirteen projects, and its 14 tests passed. The link audit found no missing files or Markdown anchors across 224 authored pages and 1,313 local or cross-repository link occurrences. Three GitHub issue/advisory interface links were outside the filesystem check. Project-file comparisons preserved all command blocks, mathematical expressions, headings, numerical tokens, and citation/link destinations. The profile's new navigation links and writing-standard section were checked separately. Whitespace checks passed in every repository.

This is an AI-assisted editorial review, not a new scientific validation or literature search. Scientific tests and full analysis reproductions were completed in the preceding maintenance pass; this prose-only pass uses documentation and content-preservation checks. It preserves the distinctions between public-data reanalysis and new experiments, exploratory and confirmatory results, computational consistency and biological validity, and future learning goals and completed work.
