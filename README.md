# Brandon J. Huynh, MPH

I’m an infectious disease and public health researcher working with biological data and mathematical models. My background is in chemistry, molecular laboratory science, epidemiology, and biostatistics. Across those fields, I keep coming back to one question: **which conclusions can these measurements support?**

## Start with a question

- **What does a gap on a surveillance map mean?** Open the Colombia Dengue Surveillance Atlas and select Bogotá. Compare its source-row coverage with a department that has reported cases. The weekly series and downloadable table let you check what the map shows. [Explore the Atlas](https://thethunda01.github.io/colombia-dengue-atlas/)
- **How much can we learn from a fitted curve?** Start with the enzyme kinetics workbench. Look at what happens to the estimated parameters when the highest concentrations are left out. Then follow the GFP and MAPK studies to see how the choice of measurements affects a prediction. [Enzyme kinetics](https://github.com/TheThunda01/enzyme-kinetics-workbench) · [Featured reading path](PROJECT_GUIDE.md#featured-reading-path)
- **Can two reviewers trace a disagreement to its source?** Load the two synthetic reviewer tables in EvidenceTrail, compare an extraction field, and follow the source locators before recording a decision. [Try EvidenceTrail](https://thethunda01.github.io/evidencetrail/)

## One result to look at

I expected a rule that combines uncertainty and diversity to help most on the more distant green fluorescent protein (GFP) variants. The archived brightness measurements let me check that expectation four times, starting the comparison with a different random seed each time.

![Distant minus local benefit in RMSE units by seed. Seed 11, +0.005. Seed 29, −0.079. Seed 47, +0.054. Seed 83, −0.097.](docs/images/gfp-distance-contrast.png)

Two runs leaned each way. On average, the combined rule improved more over random selection on the **local** examples. All four runs reuse the same evaluation observations, so this is an exploratory result. The report gives the full comparison, including the two simpler rules. [Read the GFP report](https://github.com/TheThunda01/gfp-active-learning/blob/4b27c32047288e32a647e2e8b411f3b272d6113c/experiments/uncertainty_ablation/results/report.md) · [Download the figure data](https://github.com/TheThunda01/gfp-active-learning/blob/4b27c32047288e32a647e2e8b411f3b272d6113c/experiments/uncertainty_ablation/results/distance_benefit_contrast.csv)

## Find a project

The guide covers the fourteen research and software demonstrations, the surveillance atlas, and the Beyond the Bug book project. For a visual introduction to the molecular work, try Nature’s Perfume Lab. For public-health methods, follow the Atlas with Surveillance Data Quality to see how reporting dates and denominators affect a trend. [Project guide](PROJECT_GUIDE.md) · [Nature’s Perfume Lab](https://github.com/TheThunda01/natures-perfume-lab) · [Surveillance Data Quality](https://github.com/TheThunda01/surveillance-data-quality)

I use attributed public data and labeled simulations, and I developed these projects with AI assistance. Each project explains what its inputs measure, how to reproduce its outputs, and where interpretation gets uncertain. The roadmap records the questions I plan to investigate next. [Roadmap](PORTFOLIO_PLAN.md) · [Shared standards](PORTFOLIO_STANDARDS.md) · [Glossary](docs/glossary.md) · [Sources](REFERENCES.md) · [Maintenance](MAINTENANCE.md)
