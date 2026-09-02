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

**Senior AI engineer, seven-plus years.** I work on the part that's hard after the demo works: retrieval that returns the right answer, agents that degrade loudly instead of silently, evaluation harnesses that catch regressions, and cost you can actually account for.

Founding AI engineer at Kuration AI. First AI hire at Schneider Electric's Luminous R&D, reporting to the CTO. First data hire at brainsfeed, where I led a distributed team of ten.

**Open to senior AI IC roles — Bengaluru or remote.** [irfan.ali@datacortex.in](mailto:irfan.ali@datacortex.in)

## Experience

| Role | Org | When |
| --- | --- | --- |
| Independent AI Engineer (self-employed) | DataCortex IQ · India | Dec 2025 – present |
| Founding AI Engineer | Kuration AI · Hong Kong | 2024–2025 |
| Senior Manager – Data & AI, R&D · first AI hire, reported to CTO | Luminous Power Technologies (Schneider Electric) · India | 2023–2024 |
| Data Analytics & Automation Associate | Lynk · India | 2022–2023 |
| Head of Data & Analytics · first data hire, led team of 10+ | brainsfeed · Hong Kong | 2018–2022 |

Since December 2025 I've worked independently, self-funding a focused build phase on production LLM infrastructure — evaluation, reliability, retrieval, and multi-provider routing — and open-sourcing most of it. Pre-revenue by design and by outcome. The systems below came out of it.

## Selected engineering work

Full writeups at [datacortex.in](https://datacortex.in). Every number below has a public reproduce path.

**Company-intelligence extraction pipeline** — Five stages: search → crawl → extract → deduplicate → verdict. FastAPI, DSPy, Pydantic strict JSON Schema, confidence-scored verdicts with human-review flagging, per-call cost metering. Pass 3 runs sequentially so each verdict sees already-confirmed products.

Frozen eval, 2026-09-01, 20/20 domains scored: **macro P / R / F1 = 0.771 / 0.869 / 0.795**. The writeup is mostly about the misses — including an optimizer run that made the metric worse and got reverted, and a search provider that returned HTTP 400 on empty credits so the pipeline scored zeros instead of failing loudly.

[Case study](https://datacortex.in/work/stacksift) · [Eval writeup](https://datacortex.in/writing/evaluating-stacksift-verdict-pipeline) · [Labels + rescore script](https://github.com/irfanalidv/stacksift-eval)

`FastAPI` `DSPy` `Pydantic` `LangSmith`

**Voice check-in system** — Idempotent webhook ingest, deterministic safety detection on the raw transcript *before* any LLM call, then a Groq → Hugging Face → heuristic fallback chain. Cross-session context comes from pgvector retrieval over prior calls, not a longer prompt.

[Case study](https://datacortex.in/work/reflecta)

`Next.js` `Bolna` `Groq` `pgvector`

**FMCG trade-operations app** — Party ledgers with VAT/PAN, billing, collections, credit limits, godown stock, field-visit logging, phone-width UI. Built for distributors in Nepal. No LLM in the critical path — correctness here is referential integrity and role checks, and the writeup is honest about where app-level roles should have been database policies.

[Case study](https://datacortex.in/work/godam)

`Next.js 15` `TypeScript` `Supabase`

## Open source

Twelve published Python libraries. The only numbered result is linked to its benchmark file.

| Library | What it does |
| --- | --- |
| [**RAGNav**](https://pypi.org/project/ragnav/) · [src](https://github.com/irfanalidv/RAGNav) | Hybrid BM25 + dense retrieval with RRF fusion. Navigation-first RAG for long documents. [R@3 0.956 over 500 SQuAD questions](https://github.com/irfanalidv/RAGNav/blob/main/benchmarks/results/squad_results.txt) — script and results in-repo |
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

## Applied research

- **Cross-validation framework for mental-health AI on MentalChat16K** — BERT and neural networks · *IJAINN, Dec 2025* · [DOI](https://doi.org/10.54105/ijainn.a1112.06011225)
- **Neural-symbolic topic evolution on Yelp reviews** — multi-aspect temporal topic modelling · *IJAINN, Oct 2025* · [DOI](https://doi.org/10.54105/ijainn.F1106.05061025)

ORCID: [0000-0003-0022-3047](https://orcid.org/0000-0003-0022-3047)

## Contact

[irfan.ali@datacortex.in](mailto:irfan.ali@datacortex.in) · [LinkedIn](https://www.linkedin.com/in/irfanalidv/) · [datacortex.in](https://datacortex.in)
