<div align="center">

  <img src="./banner.svg" alt="Irfan Ali, AI Engineer. I build AI products that turn messy information into data you can use." width="100%" />

  <br />

  [![Website](https://img.shields.io/badge/website-datacortex.in-00D1D1?style=flat-square)](https://datacortex.in)
  [![LinkedIn](https://img.shields.io/badge/linkedin-irfanalidv-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/irfanalidv/)
  [![PyPI](https://img.shields.io/badge/pypi-irfanalidv-3775A9?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/user/irfanalidv/)
  [![ORCID](https://img.shields.io/badge/ORCID-0000--0003--0022--3047-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0000-0003-0022-3047)
  [![Google Scholar](https://img.shields.io/badge/Google%20Scholar-Irfan%20Ali-4285F4?style=flat-square&logo=googlescholar&logoColor=white)](https://scholar.google.com/citations?user=RBoHG8sAAAAJ&hl=en)
  [![Email](https://img.shields.io/badge/email-irfan.ali%40datacortex.in-D14836?style=flat-square)](mailto:irfan.ali@datacortex.in)

</div>

<br />

**AI Engineer, based in Bengaluru.** Eight years in data and AI engineering, the last three building AI products end to end, seven of them fully remote with teams in Hong Kong, Europe and India. I build tools that turn messy information into data you can actually use — reading web pages and documents, pulling out what matters, and checking the result is right before anyone relies on it.

Master's in Data Science & AI, IISER Tirupati, 2026 (CGPA 8.9/10). English, Hindi, Bengali, and working Nepali.

**Looking for AI engineering work — Bengaluru or remote. Available immediately.** [irfan.ali@datacortex.in](mailto:irfan.ali@datacortex.in)

## Experience

| Role | Org | When |
| --- | --- | --- |
| AI Engineer | DataCortex · India | Dec 2025 – present |
| Head of AI | Kuration AI · Hong Kong | 2024–2025 |
| Senior Manager (R&D) | Luminous Power Technologies (a Schneider Electric company) · India | 2023–2024 |
| Data Analytics & Automation Associate | Lynk · India | 2022–2023 |
| Head of Data & Analytics | brainsfeed · Hong Kong | 2018–2022 |

## Things I've built

Full writeups at [datacortex.in](https://datacortex.in). Every number below comes from a published source you can check.

### Company-intelligence tool

**Finds 87% of the products a company actually sells, for about 5 cents a company.**

<p>
  <a href="https://github.com/irfanalidv/stacksift-eval"><img src="https://img.shields.io/badge/recall-87%25-00A3A3?style=flat-square" alt="Recall 87%" /></a>
  <a href="https://github.com/irfanalidv/stacksift-eval"><img src="https://img.shields.io/badge/precision-77%25-00A3A3?style=flat-square" alt="Precision 77%" /></a>
  <a href="https://github.com/irfanalidv/stacksift-eval"><img src="https://img.shields.io/badge/F1-0.795-0E7490?style=flat-square" alt="F1 0.795" /></a>
  <a href="https://github.com/irfanalidv/stacksift-eval"><img src="https://img.shields.io/badge/test%20set-20%20hand--checked%20companies-334155?style=flat-square" alt="Test set: 20 hand-checked companies" /></a>
  <a href="https://github.com/irfanalidv/stacksift-eval"><img src="https://img.shields.io/badge/full%20run-%241.10-334155?style=flat-square" alt="Full run cost $1.10" /></a>
</p>

Reads a company's website and returns the products they sell as organised data, not plain text. It works in five steps: search, read the pages, list candidate products, merge duplicates, then decide which are real. When it isn't sure, it holds the answer back for a person to check.

- **Scored, not eyeballed.** I built the test set: companies whose correct answers I checked by hand, kept fixed so every change is scored against the same list. Nothing shipped unless it held up on that set.
- **Anyone can re-check the score.** The labels, frozen predictions and scoring script are public. `python3 rescore.py` recomputes the numbers with no API keys.
- **Cheap to run.** The full 20-company evaluation cost $1.10 in model and search calls, and no company was left out of the score.

[Case study](https://datacortex.in/work/stacksift) · [Test set and scoring script](https://github.com/irfanalidv/stacksift-eval)

`FastAPI` `DSPy` `Pydantic` `LangSmith` `OpenAI`

### Voice check-in system

**Built so an AI provider outage never loses a call.**

Handles weekly check-in phone calls and writes up what was said. Running in production for evaluation.

- **Safety before any model.** Safety checks run on the raw transcript first and flag anything as critical or elevated.
- **Three layers of fallback.** If one analysis provider fails it moves to the next, then to fixed rules, instead of returning an error.
- **Each call saved exactly once,** even when the phone provider reports the same call twice.
- **Memory without giant prompts.** Context from earlier calls comes from searching past transcripts, not stuffing everything into one long prompt.

[Case study](https://datacortex.in/work/reflecta)

`Next.js` `Bolna` `Groq` `pgvector`

### Godam: trade desk for Nepal's FMCG distributors

**Co-founded and built solo. A live product that replaced four nightly notebooks with one set of books, in daily use by its first distributor.**

<p>
  <a href="https://getgodam.com"><img src="https://img.shields.io/badge/status-live%20product-00A3A3?style=flat-square" alt="Status: live product" /></a>
  <a href="https://getgodam.com"><img src="https://img.shields.io/badge/first%20deployment-daily%20use%20in%20Nepal-0E7490?style=flat-square" alt="First deployment: daily use in Nepal" /></a>
  <a href="https://getgodam.com"><img src="https://img.shields.io/badge/modules-15-334155?style=flat-square" alt="15 modules" /></a>
  <a href="https://getgodam.com"><img src="https://img.shields.io/badge/languages-EN%20%C2%B7%20%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE%E0%A4%B2%E0%A5%80%20%C2%B7%20%E0%A4%B9%E0%A4%BF%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A5%80-334155?style=flat-square" alt="Languages: English, Nepali, Hindi" /></a>
</p>

> "Before Godam, I balanced four notebooks every night — cash, godown, cheques, udhaaro."
> — Sumit Pokhrel, co-founder and first user, Suju Construction & Trading

Stock, sales, cash, cheques, credit and field visits for distributors who supply 40–80 retailers across a district, built for a phone screen.

- **Shaped by daily use.** Built in April 2026, then four rounds of features shipped from the distributor's real requests: receipts and vouchers, bill-by-bill payment matching, cheque reminders, Tally-style statements.
- **Speaks the business's language.** Statements in Nepali (Bikram Sambat) dates, VAT and PAN on every party, sauda (advance deal) book, credit aging, and one-tap PDF sharing on WhatsApp.
- **Built for the field.** Installs on any phone from the browser, because daily sales and collections are entered on the road, not at a desk.
- **Permissions that protect the books.** Owner, staff and view-only roles; view-only users can never change the accounts.
- **No AI in the critical path.** Getting the numbers right comes down to careful data handling and permissions.

[Product site](https://getgodam.com) · [Case study](https://datacortex.in/work/godam)

`Next.js` `TypeScript` `Supabase` `Postgres` `PWA`

## Open source

Python libraries I build and maintain on PyPI. Numbers below refresh daily.

<p align="center">
  <a href="https://pypi.org/user/irfanalidv/">
    <img src="./assets/impact.svg" alt="Open-source impact: Python libraries on PyPI, total and monthly downloads, releases, and downloads per library" width="100%" />
  </a>
</p>

<!-- LIBS:START -->
| Library | What it does | Live stats |
| --- | --- | --- |
| [**toxic-comment-classifier**](https://github.com/irfanalidv/toxic_comment_classifier) | Detects toxic comments, with a score per category (toxic, insult, threat and more) | [![PyPI version](https://img.shields.io/pypi/v/toxic_comment_classifier?style=flat-square&logo=pypi&logoColor=white&label=PyPI&color=3775A9)](https://pypi.org/project/toxic_comment_classifier/) [![Total downloads](https://img.shields.io/pepy/dt/toxic_comment_classifier?style=flat-square&label=downloads&color=00A3A3)](https://pepy.tech/projects/toxic_comment_classifier) |
| [**lingo-nlp-toolkit**](https://github.com/irfanalidv/lingo-nlp-toolkit) | Text-processing toolkit on Hugging Face models: classification, entities, sentiment, question answering, summarisation, embeddings | [![PyPI version](https://img.shields.io/pypi/v/lingo-nlp-toolkit?style=flat-square&logo=pypi&logoColor=white&label=PyPI&color=3775A9)](https://pypi.org/project/lingo-nlp-toolkit/) [![Total downloads](https://img.shields.io/pepy/dt/lingo-nlp-toolkit?style=flat-square&label=downloads&color=00A3A3)](https://pepy.tech/projects/lingo-nlp-toolkit) |
| [**ragfallback**](https://github.com/irfanalidv/ragfallback) | Stops a search-and-answer system failing quietly. Rewrites weak queries, scores how confident the results are, and falls back when they're poor | [![PyPI version](https://img.shields.io/pypi/v/ragfallback?style=flat-square&logo=pypi&logoColor=white&label=PyPI&color=3775A9)](https://pypi.org/project/ragfallback/) [![Total downloads](https://img.shields.io/pepy/dt/ragfallback?style=flat-square&label=downloads&color=00A3A3)](https://pepy.tech/projects/ragfallback) |
| [**nepal-gov-agent**](https://github.com/irfanalidv/Nepal-Gov-Agent) | Answers questions about Nepal government policy and legal documents, in Nepali and English, citing the sentence each answer came from | [![PyPI version](https://img.shields.io/pypi/v/nepal-gov-agent?style=flat-square&logo=pypi&logoColor=white&label=PyPI&color=3775A9)](https://pypi.org/project/nepal-gov-agent/) [![Total downloads](https://img.shields.io/pepy/dt/nepal-gov-agent?style=flat-square&label=downloads&color=00A3A3)](https://pepy.tech/projects/nepal-gov-agent) |
| [**AgentEnsemble**](https://github.com/irfanalidv/AgentEnsemble) | Running several AI agents together: routing work between them, planning, and tracking what it costs. Works with OpenAI or Mistral | [![PyPI version](https://img.shields.io/pypi/v/agentensemble?style=flat-square&logo=pypi&logoColor=white&label=PyPI&color=3775A9)](https://pypi.org/project/agentensemble/) [![Total downloads](https://img.shields.io/pepy/dt/agentensemble?style=flat-square&label=downloads&color=00A3A3)](https://pepy.tech/projects/agentensemble) |
| [**AgentCare**](https://github.com/irfanalidv/AgentCare) | Voice AI for healthcare: call intake, pulling out the details that matter, chasing missing information, booking appointments | [![PyPI version](https://img.shields.io/pypi/v/agentcare?style=flat-square&logo=pypi&logoColor=white&label=PyPI&color=3775A9)](https://pypi.org/project/agentcare/) [![Total downloads](https://img.shields.io/pepy/dt/agentcare?style=flat-square&label=downloads&color=00A3A3)](https://pepy.tech/projects/agentcare) |
| [**AskPandas**](https://github.com/irfanalidv/AskPandas) | Ask questions about a CSV in plain English. Runs on a local model by default, so nothing leaves your computer, or on OpenAI / Mistral | [![PyPI version](https://img.shields.io/pypi/v/askpandas?style=flat-square&logo=pypi&logoColor=white&label=PyPI&color=3775A9)](https://pypi.org/project/askpandas/) [![Total downloads](https://img.shields.io/pepy/dt/askpandas?style=flat-square&label=downloads&color=00A3A3)](https://pepy.tech/projects/askpandas) |
| [**RAGNav**](https://github.com/irfanalidv/RAGNav) | Search that combines keyword matching with meaning-based matching, so a question can be found either way. Answers cite the passage they came from | [![PyPI version](https://img.shields.io/pypi/v/ragnav?style=flat-square&logo=pypi&logoColor=white&label=PyPI&color=3775A9)](https://pypi.org/project/ragnav/) [![Total downloads](https://img.shields.io/pepy/dt/ragnav?style=flat-square&label=downloads&color=00A3A3)](https://pepy.tech/projects/ragnav) |
| [**PyroChain**](https://github.com/irfanalidv/PyroChain) | Using AI agents and a fine-tuned language model to work out which features matter in a dataset | [![PyPI version](https://img.shields.io/pypi/v/pyrochain?style=flat-square&logo=pypi&logoColor=white&label=PyPI&color=3775A9)](https://pypi.org/project/pyrochain/) [![Total downloads](https://img.shields.io/pepy/dt/pyrochain?style=flat-square&label=downloads&color=00A3A3)](https://pepy.tech/projects/pyrochain) |
<!-- LIBS:END -->

All packages: [pypi.org/user/irfanalidv](https://pypi.org/user/irfanalidv/)

## Papers

<p align="center">
  <a href="https://orcid.org/0000-0003-0022-3047">
    <img src="./assets/research.svg" alt="Published research: two sole-author, peer-reviewed, open-access journal papers with key results" width="100%" />
  </a>
</p>

Sole-author, peer-reviewed (double-anonymised) and open access, written at IISER Tirupati.
Research interests: natural language processing, information extraction, conversational AI, neural information retrieval.

### Advanced cross-validation framework for mental-health AI on MentalChat16K

[*Indian Journal of Artificial Intelligence and Neural Networking*](https://www.ijainn.latticescipub.com/portfolio-item/a111206011225/), vol. 6, no. 1, pp. 10–17, Dec 2025 · sole author · IISER Tirupati

<a href="https://doi.org/10.54105/ijainn.A1112.06011225"><img src="https://img.shields.io/badge/DOI-10.54105%2Fijainn.A1112.06011225-0E7490?style=flat-square&logo=doi&logoColor=white" alt="DOI 10.54105/ijainn.A1112.06011225" /></a>
<a href="https://www.ijainn.latticescipub.com/wp-content/uploads/papers/v6i1/A111206011225.pdf"><img src="https://img.shields.io/badge/read-PDF%2C%20free-00A3A3?style=flat-square&logo=adobeacrobatreader&logoColor=white" alt="Read the paper (PDF, free)" /></a>
<a href="https://www.ijainn.latticescipub.com/portfolio-item/a111206011225/"><img src="https://img.shields.io/badge/open%20access-CC%20BY--NC--ND%204.0-F68212?style=flat-square&logo=openaccess&logoColor=white" alt="Open access, CC BY-NC-ND 4.0" /></a>
<a href="https://www.ijainn.latticescipub.com/portfolio-item/a111206011225/"><img src="https://img.shields.io/badge/data-16%2C084%20conversations-334155?style=flat-square" alt="Data: 16,084 conversations" /></a>

Benchmarks conversation AI for mental-health support on 16,084 therapy conversations (6,338 real clinical interviews). A BERT classifier reaches **86.7% accuracy and 86.1% F1**, and the gaps between models are checked with McNemar's test and bootstrap confidence intervals (p < 0.05) rather than taken at face value. The paper also documents the dataset's limits, including no demographic labels, and states that clinical validation is needed before any real-world use.

<sub>Keywords: Mental health · Conversational AI · BERT · Neural networks · Sentiment analysis</sub>

### Multi-aspect temporal topic evolution for Yelp review analysis

[*Indian Journal of Artificial Intelligence and Neural Networking*](https://www.ijainn.latticescipub.com/portfolio-item/f110605061025/), vol. 5, no. 6, pp. 10–19, Oct 2025 · sole author · IISER Tirupati

<a href="https://doi.org/10.54105/ijainn.F1106.05061025"><img src="https://img.shields.io/badge/DOI-10.54105%2Fijainn.F1106.05061025-0E7490?style=flat-square&logo=doi&logoColor=white" alt="DOI 10.54105/ijainn.F1106.05061025" /></a>
<a href="https://www.ijainn.latticescipub.com/wp-content/uploads/papers/v5i6/F110605061025.pdf"><img src="https://img.shields.io/badge/read-PDF%2C%20free-00A3A3?style=flat-square&logo=adobeacrobatreader&logoColor=white" alt="Read the paper (PDF, free)" /></a>
<a href="https://www.ijainn.latticescipub.com/portfolio-item/f110605061025/"><img src="https://img.shields.io/badge/open%20access-CC%20BY--NC--ND%204.0-F68212?style=flat-square&logo=openaccess&logoColor=white" alt="Open access, CC BY-NC-ND 4.0" /></a>
<a href="https://www.ijainn.latticescipub.com/portfolio-item/f110605061025/"><img src="https://img.shields.io/badge/data-3%2C000%20reviews%20%C2%B7%20248%20metros-334155?style=flat-square" alt="Data: 3,000 reviews · 248 metros" /></a>
<a href="https://zenodo.org/records/17473209"><img src="https://img.shields.io/badge/archived-Zenodo-1682D4?style=flat-square&logo=zenodo&logoColor=white" alt="Archived on Zenodo" /></a>

Tracks what restaurant customers talk about, and how it shifts over time, across 3,000 Yelp reviews from 1,467 businesses in 248 metro areas (2005–2018). Combines transformer-based extraction (**97.2% F1** on named entities), topic modelling (eight topics, **87.5% diversity**), sentiment forecasting (17.9% mean absolute error) and city-level comparisons that are statistically tested (p < 0.05 across 10 cities).

<sub>Keywords: Topic modelling · Information extraction · Neural-symbolic learning · Temporal analysis · Business intelligence</sub>

**Journal:** Indian Journal of Artificial Intelligence and Neural Networking (IJAINN), Lattice Science Publication · ISSN 2582-7626 (online) · indexed in Crossref

<a href="https://orcid.org/0000-0003-0022-3047"><img src="https://img.shields.io/badge/ORCID-0000--0003--0022--3047-A6CE39?style=flat-square&logo=orcid&logoColor=white" alt="ORCID 0000-0003-0022-3047" /></a>
<a href="https://scholar.google.com/citations?user=RBoHG8sAAAAJ&hl=en"><img src="https://img.shields.io/badge/Google%20Scholar-verified%20at%20IISER%20Tirupati-4285F4?style=flat-square&logo=googlescholar&logoColor=white" alt="Google Scholar profile, verified email at IISER Tirupati" /></a>

## Contact

[irfan.ali@datacortex.in](mailto:irfan.ali@datacortex.in) · [LinkedIn](https://www.linkedin.com/in/irfanalidv/) · [datacortex.in](https://datacortex.in)
