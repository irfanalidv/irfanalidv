<div align="center">

  <img src="./banner.svg" alt="Irfan Ali, AI Engineer. I build AI products that turn messy information into data you can use." width="100%" />

  <br />

  [![Website](https://img.shields.io/badge/website-datacortex.in-00D1D1?style=flat-square)](https://datacortex.in)
  [![LinkedIn](https://img.shields.io/badge/linkedin-irfanalidv-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/irfanalidv/)
  [![PyPI](https://img.shields.io/badge/pypi-irfanalidv-3775A9?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/user/irfanalidv/)
  [![ORCID](https://img.shields.io/badge/ORCID-0000--0003--0022--3047-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0000-0003-0022-3047)
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

Full writeups at [datacortex.in](https://datacortex.in).

**Company-intelligence tool** — Reads a company's website and works out what products they sell, returning organised data rather than plain text. It searches, reads the pages, pulls out candidate products, merges duplicates, then decides which are real. When it isn't sure, it holds the answer back for a person to check.

I also built the test set: companies whose correct answers I checked by hand, kept fixed so every change is scored against the same list. Nothing shipped unless it held up on that set. The writeup walks through how the scoring works and what it taught me about the hard cases.

[Case study](https://datacortex.in/work/stacksift) · [Test set and scoring script](https://github.com/irfanalidv/stacksift-eval)

`FastAPI` `Python` `Pydantic`

**Voice check-in system** — Handles check-in phone calls and writes up what was said. Safety checks run on the raw transcript before any model is involved, and if one provider fails it falls back to another, then to fixed rules. Context from earlier calls comes from searching those transcripts rather than stuffing everything into one long prompt.

[Case study](https://datacortex.in/work/reflecta)

`Next.js` `Groq` `pgvector`

**Trade operations app** — Stock, billing, ledgers, credit limits and field visits for FMCG distributors, built for a phone screen. In daily use by a distributor in Nepal. No AI in the critical path here: getting the numbers right comes down to careful data handling and permissions.

[Case study](https://datacortex.in/work/godam)

`Next.js` `TypeScript` `Supabase`

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

- **Cross-validation framework for mental-health AI on MentalChat16K** — BERT and neural networks · *IJAINN, Dec 2025* · [DOI](https://doi.org/10.54105/ijainn.a1112.06011225)
- **How review topics change over time, on Yelp reviews** — tracking what customers talk about, aspect by aspect · *IJAINN, Oct 2025* · [DOI](https://doi.org/10.54105/ijainn.F1106.05061025)

ORCID: [0000-0003-0022-3047](https://orcid.org/0000-0003-0022-3047)

## Contact

[irfan.ali@datacortex.in](mailto:irfan.ali@datacortex.in) · [LinkedIn](https://www.linkedin.com/in/irfanalidv/) · [datacortex.in](https://datacortex.in)
