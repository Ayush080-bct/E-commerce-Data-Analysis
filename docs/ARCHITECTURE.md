# Architecture

This document covers **system design only** — folder layout, how services
talk to each other, and how to run/deploy the app. For what the analysis
actually found (top products, revenue trends, segment definitions, business
insights), see the [README](../README.md).

## Overview

```
┌─────────────────┐      ┌──────────────────┐      ┌───────────────────┐
│  notebook/       │      │  data/            │      │  models/           │
│  (analysis)      │ ───▶ │  raw/, processed/ │ ◀──▶ │  scaler.pkl        │
│  01 → 04         │      │                   │      │  kmeans.pkl        │
└─────────────────┘      └──────────────────┘      └─────────┬─────────┘
                                                               │
                                                               ▼
                                                    ┌──────────────────────┐
                                                    │  backend/ (FastAPI)  │
                                                    │  loads data + model  │
                                                    │  exposes REST API    │
                                                    └──────────┬───────────┘
                                                               │ HTTP (JSON)
                                                               ▼
                                                    ┌──────────────────────┐
                                                    │  dashboard/          │
                                                    │  (Streamlit)         │
                                                    │  calls the API,      │
                                                    │  renders UI          │
                                                    └──────────────────────┘
```

The notebooks are where the actual data science happens (cleaning, RFM
scoring, clustering). Everything after that — backend and frontend — exists
to serve the *output* of that analysis (the cleaned data + the trained
model) as an interactive tool, without re-running any notebook.

## Project structure

```
├── data/
│   ├── raw/            # original, untouched source data (data.csv)
│   └── processed/      # outputs of the notebooks
│       ├── data_clean.csv   # cleaned transactional data
│       └── rfm.csv          # one row per customer: R/F/M values, scores, segment
│
├── models/
│   ├── scaler.pkl       # StandardScaler fit on Recency/Frequency/Monetary
│   └── kmeans.pkl       # trained KMeans model (k=3)
│
├── notebook/            # exploratory / one-time analysis (source of truth for *how* results were produced)
│   ├── 01_data_cleaning.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_cus_segementation.ipynb   # RFM scoring + rule-based segment labels
│   └── 04_clustering.ipynb          # StandardScaler + KMeans, saves models/
│
├── src/                 # reusable functions extracted from the notebooks
│   ├── data_cleaning.py     # load_path, drop_missing_customers, convert_invoice_date, save_clean_data
│   ├── segementFunc.py      # segement_customer(row) -> rule-based segment label
│   └── clustering.py
│
├── backend/              # FastAPI app — serves data + model over HTTP
│   ├── main.py            # creates the app, registers routes, loads data on startup
│   ├── config.py          # file paths (data/processed/rfm.csv, models/*.pkl)
│   ├── schemas.py          # Pydantic request/response models
│   ├── store.py            # DataStore: loads CSV + model once, holds in memory
│   └── routes.py            # /health, /overview, /clusters/scatter, /customers, /customers/{id}, /predict
│
├── dashboard/             # Streamlit app — the user-facing UI
│   └── app.py               # calls the backend API, renders charts/tables/forms
│
└── docs/
    └── ARCHITECTURE.md     # this file
```

## Data flow

See the [README](../README.md) for what each analysis phase actually found;
this section only tracks which file produces which artifact, for anyone
wiring up the app.

| Stage | Produces | Consumed by |
|---|---|---|
| `notebook/01_data_cleaning.ipynb` | `data/processed/data_clean.csv` | `02`, `03` |
| `notebook/03_cus_segementation.ipynb` | `data/processed/rfm.csv` (RFM values + rule-based `segment`) | `04`, `backend/store.py` |
| `notebook/04_clustering.ipynb` | `models/scaler.pkl`, `models/kmeans.pkl` | `backend/store.py` |
| `backend/store.py` | in-memory `DataStore` (rfm + `Cluster` column + segment lookup), loaded once at API startup | `backend/routes.py` |
| `backend/routes.py` (via `main.py`) | JSON over HTTP | `dashboard/app.py` |

The one thing worth calling out that *isn't* in the README: `backend/store.py`
re-runs `kmeans.predict()` on `rfm.csv` at startup rather than assuming a
`Cluster` column already exists in the CSV — so the API is the single
source of truth for cluster assignment, not the notebook output.

## Backend (FastAPI)

Runs as its own process (`uvicorn backend.main:app --reload`), independent
of the frontend. Responsibilities:

| Endpoint | Purpose |
|---|---|
| `GET /health` | liveness check + row count |
| `GET /overview` | segment counts, revenue by segment, summary stats |
| `GET /clusters/scatter` | per-customer RFM + cluster, for plotting |
| `GET /customers` | list of all customer IDs |
| `GET /customers/{id}` | full RFM detail + cluster for one customer |
| `POST /predict` | scale + `kmeans.predict()` a new (recency, frequency, monetary) triple |

All data/model loading happens once in `store.py` and is shared across
requests via FastAPI's dependency injection (`Depends(get_store)`) rather
than being reloaded per request.

## Frontend (Streamlit)

`dashboard/app.py` is a pure API client: it calls the backend with
`requests`, caches responses briefly with `st.cache_data`, and renders
Plotly charts / tables / sliders. It holds no data-science logic itself —
if the backend is down, it shows a clear error instead of failing silently.

## Why split backend/frontend at all

For a project this size a single Streamlit script would work fine
functionally. The split exists to:
- keep the model-serving logic reusable (any future client — mobile, another
  dashboard, a script — can hit the same API)
- let each half be developed, tested, and deployed independently
- demonstrate REST API design, not just an analysis script

## Running locally

```bash
pip install -r requirements-dashboard.txt

# terminal 1
uvicorn backend.main:app --reload

# terminal 2
streamlit run dashboard/app.py
```

## Deployment (planned)

- **Backend** → Render or Railway (free tier)
- **Frontend** → Streamlit Community Cloud, with `API_BASE_URL` set as an
  environment variable pointing at the deployed backend URL