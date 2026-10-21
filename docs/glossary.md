# A guide to the portfolio's vocabulary

These definitions explain how terms are used in this collection. Each project's glossary adds the details needed to follow its equations, files, and results. Definitions help with reading; they do not establish that a model's assumptions hold.

## Biology and measurements

| Term | Meaning here |
| --- | --- |
| Computational biology | Using mathematical and computational methods to investigate biological questions. |
| Molecular biology | The study of biological molecules and the processes they participate in. |
| Systems biology | Studying interactions among components and how those interactions shape a system's behavior. |
| Mechanism | A proposed causal account of how a process works. An accurate prediction alone does not establish it. |
| Enzyme, substrate, kinetics | An enzyme catalyzes a reaction; a substrate is a reactant it acts on; kinetics concerns reaction rates. |
| Apparent parameter | A fitted quantity conditional on the measurement and model. It need not equal an isolated molecular property. |
| Michaelis–Menten model | A saturating relationship between substrate concentration and rate under specific kinetic assumptions. |
| Protein structure, residue | A protein's spatial arrangement; a residue is an amino-acid unit within its chain. |
| GFP | Green fluorescent protein, whose measured fluorescence is the outcome in the retrospective learning example. |
| MAPK | Mitogen-activated protein kinase; a family of signaling proteins. The MAPK project uses a simplified cascade model. |
| Phenotype, morphology, perturbation | An observable characteristic; morphology concerns form and appearance; a perturbation changes a system's conditions. |
| Cell Painting | An imaging assay using multiple stains and computational features to describe cellular morphology. |
| DMSO | Dimethyl sulfoxide, a solvent used as a vehicle control in the morphology dataset. |
| RNA, RNA-seq | Ribonucleic acid; RNA sequencing measures sequence-derived evidence about RNA abundance and composition. Counts depend on processing and are not direct molecule counts. |
| NAAT | Nucleic acid amplification test, a test that detects targeted genetic material after amplification. |
| Positivity, prevalence | Positivity is the fraction of reported tests that are positive; prevalence is the fraction of a defined population with a condition. Their denominators differ. |

## Models, statistics, and evaluation

| Term | Meaning here |
| --- | --- |
| AI, machine learning, LLM | Artificial intelligence; machine learning fits patterns from data; a large language model generates or evaluates language using learned patterns. No current project is a validated autonomous scientist. |
| Mechanistic model | A mathematical model whose relationships represent a proposed process. Its fit does not prove the process is correct. |
| Parameter, hypothesis | A quantity that specifies a model; a proposed explanation or, in the MAPK grid, one candidate parameter combination. |
| Identifiability | Whether available observations can distinguish parameters or explanations under the assumed model. |
| Differential equation, trajectory | An equation describing rates of change; a trajectory is the resulting course through time. |
| Stoichiometry, flux | Reaction input/output proportions; flux is a modeled rate through a reaction. |
| FBA, FVA | Flux balance analysis optimizes an objective under steady-state network constraints. Flux variability analysis finds allowed individual flux ranges under declared constraints. These ranges are not confidence intervals. |
| Residual, uncertainty | A residual is a difference between observed and predicted values; each project must specify the sign convention. Uncertainty describes what is not known and must be qualified by its source and assumptions. |
| Bayesian update, posterior | Revising probabilities using observations and a likelihood; the posterior is the resulting distribution conditional on the prior and model. |
| Off-grid | Absent from the finite candidate grid. In this portfolio's MAPK stress case, the true values are still inside the grid's parameter ranges. |
| Extrapolation | Prediction beyond the domain represented by available observations or model candidates; specify which domain is meant. |
| Active learning, acquisition policy | Selecting which labels to reveal next; the acquisition policy is the selection rule. Here, archived labels or simulated measurements are used. |
| Closed-loop modeling | Repeatedly fitting a model, selecting a measurement, observing its result, and updating the model. The current loops are computational. |
| Ablation | Comparing a method's components separately to examine their contributions under matched conditions. |
| Seed, replicate | A seed initializes a pseudorandom number generator. A rerun with another seed is computational repetition, not an independent biological experiment. |
| Feature, descriptor, representation | A model input; a descriptor summarizes a property; a representation is the collection or encoding of inputs. |
| SMILES, scaffold | SMILES is a text notation for chemical structures. A scaffold is a selected core structure used here to group molecules. |
| Training, validation, test | Data used to fit a model, select its settings, and evaluate it. Observed test outcomes reused for decisions become development information. |
| Holdout, cross-validation, nested CV | A reserved evaluation set; evaluation through partitions; nested cross-validation separates model selection inside each outer evaluation partition. |
| Leakage | Evaluation information influencing a step that is supposed to use development information only. |
| Generalization, distribution shift | Performance on relevant new examples; a difference between the data-generating conditions of development and use. |
| Calibration | Agreement between stated probabilities or uncertainty levels and observed frequencies in a defined evaluation setting. |
| RMSE, MAE | Root mean squared error gives larger errors more weight; mean absolute error averages error magnitudes. Both retain the outcome's units. |
| Accuracy, precision, recall, F1 | Fraction correct; fraction of predicted positives that are positive; fraction of actual positives recovered; harmonic mean of precision and recall. |
| Macro average, average precision | A macro average weights classes equally. Average precision summarizes precision at ranks where relevant items occur, using the implemented definition. |
| PCA, normalization | Principal component analysis summarizes directions of variation; normalization adjusts measurements using a declared rule. Neither automatically removes unwanted biological or technical effects. |
| Confounding, batch effect | Entangled influences that prevent a simple attribution; a batch effect is variation associated with processing groups. |
| Independent experimental unit | The unit that can reasonably be treated as independently generated for the question. Different rows or chemical identifiers do not prove independence. |

## Software and evidence records

| Term | Meaning here |
| --- | --- |
| QC, schema, input/output contract | Quality control; a specification of fields and types; a description of accepted inputs, produced outputs, and failure behavior. |
| FASTA, FASTQ, paired-end reads | FASTA stores sequence records; FASTQ also stores quality characters; paired-end reads come from two ends of a sequencing fragment. |
| Streaming | Processing records incrementally instead of loading the entire file into memory. |
| SQL, CSV, JSON | Structured Query Language for tabular queries; comma-separated values; JavaScript Object Notation for structured records. |
| Provenance, snapshot, pinned version | A record of origins and transformations; a captured state; an explicitly fixed release, commit, or file. |
| Commit, checksum, digest | A version-control record; a value computed from bytes to detect changes; “digest” is used here for a cryptographic checksum. Matching hashes do not prove scientific truth. |
| CI, test, regression | Continuous integration runs automated checks; a test checks specified behavior; a regression is loss of behavior that previously worked. |
| Reproducibility | Here, rerunning a specified computation with the recorded inputs and environment to obtain consistent results. It is distinct from independent biological replication. |
| DOI, PMID, accession | Digital Object Identifier; PubMed identifier; a database's record identifier. These locate sources, not certify their conclusions. |
| Full-text access, abstract-only appraisal | Relevant article sections were read; only the abstract and metadata were available. The audit distinguishes them and records partial retrievals. |
| Systematic review, rapid review | A review using explicit systematic methods; a review with declared time-saving restrictions. A logged search alone does not establish either label's methodological quality. |
| PRISMA-S, FAIR4RS, CODE, TOP | Search-reporting guidance; Findable, Accessible, Interoperable, Reusable principles for research software; Open, Document, Execute, Collaborate recommendations; Transparency and Openness Promotion guidelines. See [References](../REFERENCES.md). |
| CC BY, CC0, MIT, noncommercial | Distinct reuse terms: attribution-based Creative Commons license; public-domain dedication; a permissive software license; a restriction on commercial reuse where specified. Code and data can have different terms. |

Return to the [project guide](../PROJECT_GUIDE.md), [assumptions](assumptions.md), or [review record](review-2026-10-20.md).
