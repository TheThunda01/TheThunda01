# Brandon J. Huynh, MPH

**Infectious Disease and Public Health Researcher exploring computational biology and mathematical modeling.**

## From biological measurements to better experiments

**What can we trust in a measurement, what can a model explain, and what should we measure next?**

My background spans chemistry, molecular laboratory science, epidemiology, and biostatistics. This portfolio connects those interests through public-data analyses, biological models, and tools for tracing evidence. The common thread is making the reasoning behind a result inspectable.

## Start here

Three studies introduce the main question. They use different biological systems; this is a reading path, not a single analysis pipeline.

| Study | Question | What to look for |
| --- | --- | --- |
| **1. [Enzyme kinetics](https://github.com/TheThunda01/enzyme-kinetics-workbench)** | Can different explanations fit the same measurements? | How the measured concentration range changes parameter uncertainty. |
| **2. [GFP policy comparison](https://github.com/TheThunda01/gfp-active-learning/tree/main/experiments/uncertainty_ablation)** | Does a more elaborate selection rule actually help? | A recorded expectation, a matched comparison, and an unexpected result. |
| **3. [MAPK dynamics](https://github.com/TheThunda01/mapk-dynamics-lab)** | Which observation would distinguish competing explanations? | A simulated cycle of choosing a measurement and updating model hypotheses. |

## Current investigation

The green fluorescent protein (GFP) comparison tests ways to select existing brightness measurements under a fixed budget. Across four seeds, diversity-only selection had the lowest mean error on more-distant variants; uncertainty-only selection had the lowest mean error on local variants. The combined policy did not support the prediction that it would help most at distance. These are [exploratory results on reused public outcomes](https://github.com/TheThunda01/gfp-active-learning/blob/main/experiments/uncertainty_ablation/results/report.md).

The next planned analysis asks whether the combined policy's shortlist excludes useful candidates. After that, the direction is to test when measurement selection fails in the mitogen-activated protein kinase (MAPK) simulation. The [roadmap](PORTFOLIO_PLAN.md) separates these proposals from completed work.

## Explore the supporting work

- **A public-health connection:** [Surveillance data quality](https://github.com/TheThunda01/surveillance-data-quality) examines denominators and reporting windows before interpreting a trend.
- **A research workflow tool:** [EvidenceTrail](https://github.com/TheThunda01/evidencetrail) makes extraction records and reviewer decisions inspectable. [Try its browser demo](https://thethunda01.github.io/evidencetrail/) with synthetic examples.
- **A visual introduction:** [Nature's Perfume Lab](https://github.com/TheThunda01/natures-perfume-lab) explores plant aroma chemistry and protein evidence through a familiar question.

The [complete project guide](PROJECT_GUIDE.md) places all fourteen projects in this story, including sequence and expression quality, model evaluation, structure and metabolism, and evidence-review planning.

## Methods and transparency

These projects use attributed public data and labeled simulations; they do not report new laboratory experiments I conducted or establish new biological findings. They were developed with AI assistance. Tests check specified software behavior; scientific interpretation remains tied to the evidence and limitations in each project.

[Project guide](PROJECT_GUIDE.md) · [Roadmap](PORTFOLIO_PLAN.md) · [Shared standards](PORTFOLIO_STANDARDS.md) · [Glossary](docs/glossary.md) · [Sources](REFERENCES.md) · [Maintenance and review history](MAINTENANCE.md)
