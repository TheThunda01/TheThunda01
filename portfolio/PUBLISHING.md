# Publishing the four projects

Each project directory is a standalone repository root. Its `.github/workflows/` directory belongs at the root of the eventual repository, where GitHub Actions can discover it. The combined review copy also has a separate workflow for checking the projects together.

## Intended repositories

| Owner | Name | Suggested description |
| --- | --- | --- |
| TheThunda01 | pasilla-expression-qc | Reproducible Drosophila expression-data QC with explicit normalization and PCA limits. |
| TheThunda01 | sequence-quality-toolkit | A tested Python CLI for FASTA and manifest checks using synthetic examples. |
| TheThunda01 | surveillance-data-quality | Python and SQLite audits of synthetic reporting data, missingness, and denominators. |
| TheThunda01 | cell-feature-model-validation | An educational biological-feature benchmark with training-only tuning and held-out evaluation. |

Create public repositories containing these project files and their own licenses, then update the profile links to point to them. Do not make an empty project repository appear complete: retain the example results, methods, provenance, and tests.

If publishing manually, create each empty repository on GitHub without an initial README, license, or ignore file. Copy the corresponding project directory, including its `.github` directory, into a local Git checkout, commit it, add the new repository as `origin`, and push `main`. The GitHub web interface also supports uploading files, but check that hidden workflow directories were included.

Keep the existing EvidenceTrail and portfolio-site repositories intact. The combined review branch is a temporary place to inspect this work; it does not need to be merged into the profile repository as a permanent monorepo.

After publication, run each repository's Actions workflow, check its rendered README and relative links, and pin the desired projects on the profile. Do not describe remote CI as passing until a completed run confirms it. Add a release tag only after these checks.

The GitHub connector used for this preparation supports editing existing repositories but does not expose repository creation. A supported browser handoff or a manual creation step is still required for the four separate repositories.
