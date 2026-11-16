# Diesel-Radar

Fuel price analytics pipeline for the Kehl border region (Germany / France).

Tracks diesel prices from public pump data, models price cycles,
and estimates monthly savings for logistics operations.

![CI](https://github.com/Mamine-ai/diesel-radar/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Why

Fuel is 25–35 % of variable transport costs in road logistics.
Small price differences across the DE/FR border add up fast
when you operate daily routes through Kehl.

This project pulls open pump data, runs a forecast model,
and shows when and where to refuel to cut costs.

---

## Stack

| Layer | Tool |
|---|---|
| Ingestion | Python · httpx |
| Storage | DuckDB |
| Transform | dbt-duckdb |
| Forecast | LightGBM |
| Dashboard | Streamlit |
| CI | GitHub Actions · uv |

---

## Data source

Tankerkönig open data — license CC BY 4.0  
All German stations · prices updated every 15 min  
Study area: Kehl + 30 km radius (48.57 N, 7.81 E)

---

## Quickstart

```bash
git clone https://github.com/Mamine-ai/diesel-radar.git
cd diesel-radar
uv sync --all-extras --dev
cp .env.example .env
# add your keys to .env
uv run pytest -q
```

---

## Project status

| Phase | Description | Status |
|---|---|---|
| 0 | Environment setup | ✅ done |
| 1 | CI pipeline · README | ✅ done |
| 2 | Data ingestion | in progress |
| 3 | DuckDB · dbt transforms | — |
| 4 | EDA · KPIs | — |
| 5 | Price forecast model | — |
| 6 | Savings calculator | — |
| 7 | Streamlit app · Docker | — |

---

## Author

Mohammed  Laabidi
Logistics trainee · self-taught in data engineering and analytics  
Kehl, Germany
