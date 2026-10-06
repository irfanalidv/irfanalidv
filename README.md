<div align="center">

  <img src="./banner.svg" alt="Irfan Ali — AI Engineer. I build tools that turn messy information into data you can use." width="100%" />

  <br />

  [![Website](https://img.shields.io/badge/website-datacortex.in-00D1D1?style=flat-square)](https://datacortex.in)
  [![LinkedIn](https://img.shields.io/badge/linkedin-irfanalidv-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/irfanalidv/)
  [![PyPI](https://img.shields.io/badge/pypi-irfanalidv-3775A9?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/user/irfanalidv/)
  [![ORCID](https://img.shields.io/badge/ORCID-0000--0003--0022--3047-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0000-0003-0022-3047)
  [![Email](https://img.shields.io/badge/email-irfan.ali%40datacortex.in-D14836?style=flat-square)](mailto:irfan.ali@datacortex.in)

</div>

<br />

**AI Engineer, based in Bengaluru.** I build tools that turn messy information into data you can actually use — reading web pages and documents, pulling out what matters, and checking the result is right before anyone relies on it.

Master's in Data Science & AI, IISER Tirupati, 2026.

**Looking for AI engineering work — Bengaluru or remote. Available immediately.** [irfan.ali@datacortex.in](mailto:irfan.ali@datacortex.in)

## Experience

| Role | Org | When |
| --- | --- | --- |
| AI Engineer | DataCortex · India | Dec 2025 – present |
| Head of AI | Kuration AI · Hong Kong | 2024–2025 |
| Senior Manager – Data & AI, R&D | Luminous Power Technologies · India | 2023–2024 |
| Data Analytics & Automation Associate | Lynk · India | 2022–2023 |
| Head of Data & Analytics | brainsfeed · Hong Kong | 2018–2022 |

## Things I've built

Full writeups at [datacortex.in](https://datacortex.in). Everything below has a public repo you can check.

**Company-intelligence tool** — Reads a company's website and works out what products they sell, returning organised data rather than plain text. Five steps: search, read the pages, pull out candidate products, merge duplicates, then decide which are real. Results that aren't confident get flagged for a person to check instead of being trusted automatically.

I also built the test set: a group of companies where I'd worked out the correct answer by hand, kept fixed, so I could tell whether a change made the tool better or worse. The writeup is mostly about where it got things wrong — including a change I was confident about that made accuracy worse and got reverted.

[Case study](https://datacortex.in/work/stacksift) · [Test set and scoring script](https://github.com/irfanalidv/stacksift-eval)

`FastAPI` `Python` `Pydantic`

**Voice check-in system** — Handles check-in phone calls and writes up what was said. Safety checks run on the raw transcript before any model is involved, and if one provider fails it falls back to another, then to fixed rules. Context from earlier calls comes from searching those transcripts rather than stuffing everything into one long prompt.

[Case study](https://datacortex.in/work/reflecta)

`Next.js` `Groq` `pgvector`

**Trade operations app** — Stock, billing, ledgers, credit limits and field visits for FMCG distributors, built for a phone screen. In daily use by a distributor in Nepal. No AI in the critical path here — getting the numbers right is about careful data handling and permissions, and the writeup is honest about where I'd do that differently.

[Case study](https://datacortex.in/work/godam)

`Next.js` `TypeScript` `Supabase`

## Open source

Python libraries published on PyPI.

| Library | What it does |
| --- | --- |
| [**RAGNav**](https://pypi.org/project/ragnav/) · [src](https://github.com/irfanalidv/RAGNav) | Search that combines keyword matching with meaning-based matching, so a question can be found either way. On [500 test questions, the right passage was in the top three 95.6% of the time](https://github.com/irfanalidv/RAGNav/blob/main/benchmarks/results/squad_results.txt) — script and results in the repo |
| [**ragfallback**](https://pypi.org/project/ragfallback/) · [src](https://github.com/irfanalidv/ragfallback) | Stops a search-and-answer system failing quietly. Rewrites weak queries, scores how confident the results are, and falls back when they're poor |
| [**AgentEnsemble**](https://pypi.org/project/agentensemble/) · [src](https://github.com/irfanalidv/AgentEnsemble) | Running several AI agents together — routing work between them, planning, and tracking what it costs |
| [**nepal-gov-agent**](https://pypi.org/project/nepal-gov-agent/) · [src](https://github.com/irfanalidv/Nepal-Gov-Agent) | Answers questions about Nepal government policy and legal documents, in Nepali and English, citing the sentence each answer came from |
| [**AgentCare**](https://pypi.org/project/agentcare/) · [src](https://github.com/irfanalidv/AgentCare) | Voice AI for healthcare — call intake, pulling out the details that matter, chasing missing information, booking appointments |
| [**scrapeflow-py**](https://pypi.org/project/scrapeflow-py/) · [src](https://github.com/irfanalidv/scrapeflow-py) | Reading data off websites with Playwright — handles sessions, rate limits and pages that try to block you |
| [**AskPandas**](https://pypi.org/project/askpandas/) · [src](https://github.com/irfanalidv/AskPandas) | Ask questions about a CSV in plain English, using a model running on your own machine. No API keys, nothing leaves your computer |
| [**lingo-nlp-toolkit**](https://pypi.org/project/lingo-nlp-toolkit/) · [src](https://github.com/irfanalidv/lingo-nlp-toolkit) | Small text-processing utilities that work with both older pipelines and newer models |
| [**PyroChain**](https://pypi.org/project/pyrochain/) · [src](https://github.com/irfanalidv/PyroChain) | Using AI agents to work out which features matter in a dataset |
| [**toxic-comment-classifier**](https://pypi.org/project/toxic-comment-classifier/) · [src](https://github.com/irfanalidv/toxic_comment_classifier) | Detects toxic comments, with a score per category |
| [**socialmediaextractor**](https://pypi.org/project/socialmediaextractor/) · [src](https://github.com/irfanalidv/socialmediaextractor) | Pulls social media profile links out of websites |
| [**trustpilot-scraper**](https://pypi.org/project/trustpilot-scraper/) · [src](https://github.com/irfanalidv/trustpilot_scraper) | Collects Trustpilot reviews into a structured file |

All packages: [pypi.org/user/irfanalidv](https://pypi.org/user/irfanalidv/)

## Papers

- **Cross-validation framework for mental-health AI on MentalChat16K** — BERT and neural networks · *IJAINN, Dec 2025* · [DOI](https://doi.org/10.54105/ijainn.a1112.06011225)
- **Neural-symbolic topic evolution on Yelp reviews** — multi-aspect temporal topic modelling · *IJAINN, Oct 2025* · [DOI](https://doi.org/10.54105/ijainn.F1106.05061025)

ORCID: [0000-0003-0022-3047](https://orcid.org/0000-0003-0022-3047)

## Contact

[irfan.ali@datacortex.in](mailto:irfan.ali@datacortex.in) · [LinkedIn](https://www.linkedin.com/in/irfanalidv/) · [datacortex.in](https://datacortex.in)
