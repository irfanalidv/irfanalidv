<div align="center">

  <img src="./banner.svg" alt="Irfan Ali — Senior AI Engineer. I make LLM systems reliable in production." width="100%" />

  <br />

  [![Website](https://img.shields.io/badge/website-datacortex.in-00D1D1?style=flat-square)](https://datacortex.in)
  [![LinkedIn](https://img.shields.io/badge/linkedin-irfanalidv-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/irfanalidv/)
  [![PyPI](https://img.shields.io/badge/pypi-12_libraries-3775A9?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/user/irfanalidv/)
  [![ORCID](https://img.shields.io/badge/ORCID-0000--0003--0022--3047-A6CE39?style=flat-square&logo=orcid&logoColor=white)](https://orcid.org/0000-0003-0022-3047)
  [![Email](https://img.shields.io/badge/email-irfan.ali%40datacortex.in-D14836?style=flat-square)](mailto:irfan.ali@datacortex.in)

</div>

<br />

Seven-plus years building AI and data systems. Previously founding AI engineer at Kuration AI in Hong Kong, and the first AI hire at Schneider Electric in India, reporting to the CTO.

Independent AI engineer (self-employed) — DataCortex IQ · Dec 2025–present · self-funded, pre-revenue.

**Open to senior AI IC roles — Bengaluru or remote.**

<table>
  <tr>
    <td align="center">12 PyPI libraries</td>
    <td align="center">2 peer-reviewed papers</td>
    <td align="center">First AI hire, twice</td>
    <td align="center">Startups + enterprise</td>
  </tr>
</table>

## Selected work

Engineering writeups on [datacortex.in](https://datacortex.in). Metrics below have a public reproduce path.

### [Stacksift](https://stacksift.in) · company intelligence

Five-stage pipeline: search → crawl → extract → deduplicate → verdict. FastAPI, DSPy, Pydantic strict JSON Schema, sequential Pass 3 so each call sees already-confirmed products.

Frozen eval (2026-09-01, 20/20 scored): **macro P / R / F1 = 0.771 / 0.869 / 0.795**. The writeup is the misses.

[Case study](https://datacortex.in/work/stacksift) · [Eval writeup](https://datacortex.in/writing/evaluating-stacksift-verdict-pipeline) · [Labels + rescore](https://github.com/irfanalidv/stacksift-eval)

`FastAPI` `DSPy` `Pydantic` `LangSmith`

### [Reflecta](https://getreflecta.com) · voice check-ins

Idempotent Bolna webhook ingest, deterministic crisis detection on the raw transcript **before** any LLM call, then Groq → Hugging Face → heuristic analysis. Prior-call context via Neon Postgres / pgvector — not a longer prompt.

[Case study](https://datacortex.in/work/reflecta)

`Next.js` `Bolna` `Groq` `pgvector`

### [Godam](https://getgodam.com) · FMCG trade operations

Trade-ops app for Nepal distributors: party ledgers (VAT/PAN), billing, collections, credit, godown stock, DSR, field-visit logging. Phone-width UI. Built solo. No LLM in the critical path — reliability is referential integrity and role checks.

[Case study](https://datacortex.in/work/godam)

`Next.js 15` `TypeScript` `Supabase`

## Previously

| Role | Org | When |
| --- | --- | --- |
| Founding AI Engineer | Kuration AI · Hong Kong | 2024–2025 |
| Senior Manager – Data & AI, R&D · first AI hire, reported to CTO | Luminous Power Technologies (Schneider Electric) · India | 2023–2024 |
| Data Analytics & Automation Associate | Lynk | 2022–2023 |
| Head of Data & Analytics · first data hire | brainsfeed · Hong Kong | 2018–2022 |

## Open source

Twelve published Python libraries. Descriptions match the packages; the only numbered retrieval result is linked to the benchmark file.

| Library | What it does |
| --- | --- |
| [**RAGNav**](https://pypi.org/project/ragnav/) · [src](https://github.com/irfanalidv/RAGNav) | Hybrid BM25 + dense retrieval with RRF fusion. Navigation-first RAG for long documents. [R@3 0.956 over 500 SQuAD questions](https://github.com/irfanalidv/RAGNav/blob/main/benchmarks/results/squad_results.txt) |
| [**ragfallback**](https://pypi.org/project/ragfallback/) · [src](https://github.com/irfanalidv/ragfallback) | Stop RAG from failing silently. Query rewriting, retrieval confidence scoring, fallback strategies, retry logic |
| [**AgentEnsemble**](https://pypi.org/project/agentensemble/) · [src](https://github.com/irfanalidv/AgentEnsemble) | Multi-agent orchestration. ReAct, Swarm, Pipeline, Debate, WorkflowGraph. Routing, planning, RAG, cost tracking |
| [**nepal-gov-agent**](https://pypi.org/project/nepal-gov-agent/) · [src](https://github.com/irfanalidv/Nepal-Gov-Agent) | Agentic RAG on Nepal government policy and legal documents. Hybrid retrieval with citations. Nepali + English |
| [**AgentCare**](https://pypi.org/project/agentcare/) · [src](https://github.com/irfanalidv/AgentCare) | Voice AI for healthcare. Call intake, structured extraction, missing-data recovery, appointment orchestration |
| [**scrapeflow-py**](https://pypi.org/project/scrapeflow-py/) · [src](https://github.com/irfanalidv/scrapeflow-py) | Playwright scraping. LLM extraction, hybrid selectors, session persistence, rate limiting, anti-detection |
| [**AskPandas**](https://pypi.org/project/askpandas/) · [src](https://github.com/irfanalidv/AskPandas) | Natural-language queries on CSV via local LLMs. No API keys, no cloud |
| [**lingo-nlp-toolkit**](https://pypi.org/project/lingo-nlp-toolkit/) · [src](https://github.com/irfanalidv/lingo-nlp-toolkit) | Lightweight NLP utilities bridging classic pipelines and transformer-ready workflows |
| [**PyroChain**](https://pypi.org/project/pyrochain/) · [src](https://github.com/irfanalidv/PyroChain) | Agentic feature engineering. PyTorch + LangChain agents for multimodal extraction |
| [**toxic-comment-classifier**](https://pypi.org/project/toxic-comment-classifier/) · [src](https://github.com/irfanalidv/toxic_comment_classifier) | Deep-learning toxicity detection with per-category scores |
| [**socialmediaextractor**](https://pypi.org/project/socialmediaextractor/) · [src](https://github.com/irfanalidv/socialmediaextractor) | Extract social media profile links from websites |
| [**trustpilot-scraper**](https://pypi.org/project/trustpilot-scraper/) · [src](https://github.com/irfanalidv/trustpilot_scraper) | Scrape Trustpilot reviews into structured output |

All packages: [pypi.org/user/irfanalidv](https://pypi.org/user/irfanalidv/)

## Publications

- **Mental Health AI on MentalChat16K** — BERT + neural networks on a cross-validation framework · *IJAINN, Dec 2025* · [DOI](https://doi.org/10.54105/ijainn.a1112.06011225)
- **Neural-Symbolic Topic Evolution on Yelp Reviews** — multi-aspect temporal topic modelling · *IJAINN, Oct 2025* · [DOI](https://doi.org/10.54105/ijainn.F1106.05061025)

ORCID: [0000-0003-0022-3047](https://orcid.org/0000-0003-0022-3047)

## Contact

[irfan.ali@datacortex.in](mailto:irfan.ali@datacortex.in) · [LinkedIn](https://www.linkedin.com/in/irfanalidv/) · [datacortex.in](https://datacortex.in)

---

<div align="center">
  <sub>Reliability over hype · Systems over scripts · Maintainability over short-term hacks</sub>
</div>
