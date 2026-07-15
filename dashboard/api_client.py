"""
Thin client for the fastapi backend, shared by everypage.
Nothing in here renders ui - it only fetches/parses data.
"""

import os
import pandas as pd
import requests
import streamlit as st

API_BASE_URL = os.environ.get("API_BASE_URL", "http://localhost:8000")

def _get(path:str, **kwargs):
    """Send a GET request to the backend and return the JSON response."""
    r = requests.get(f"{API_BASE_URL}{path}", timeout=10, **kwargs)
    r.raise_for_status()
    return r.json()

def _post(path:str,json_body:dict):
    """ Send a POST request to the backend with a JSON body and return the JSON response."""
    r = requests.post(f"{API_BASE_URL}{path}", json=json_body, timeout=10)
    r.raise_for_status()
    return r.json()

# Unlike TypeScript, Python does not enforce type safety at compile time.
# Therefore, we use generic helper functions (_get and _post) to centralize
# request logic, error handling, and JSON parsing. Streamlit pages import
# this module to fetch/submit data without duplicating request code.

def check_backend_alive()->bool:
    try:
        _get("/health")
        return True
    except requests.exceptions.RequestException:
        return False

def require_backend():
    """
    Call at the top of the every page. Stops the page with clear error if backend isnot reachable, instead of letting
    requests fail deep inside the page logic."""
    if not check_backend_alive():
        st.error(
            f"can't reach the backend API at `{API_BASE_URL}`.\n\n"\
            "start it first with:\n\n"
            "```bash\nuvicorn backend.main:app --reload\n```\n\n"
            "then Reload this page"
            )
        st.stop()

@st.cache_data(ttl=60)
def fetch_overview() -> dict:
    return _get("/overview")

@st.cache_data(ttl=60)
def fetch_scatter_df()->pd.DataFrame:
    return pd.DataFrame(_get("/cluster/scatter"))

@st.cache_data(ttl=60)
def fetch_customer_ids() -> list[str]:
    return _get("/customers")

def fetch_customer(customer_id:str) -> dict | None:
    try:
        return _get(f"/customers/{customer_id}")
    except requests.HTTPError as e:
        if e.response is not None and e.response.status_code == 404:
            return None
        raise

def call_predict(recency: float, frequency: float, monetory: float) -> dict:
    return _post(
        "/predict",
        {
            "recency":recency,
            "frequency":frequency,
            "monetory":monetory
        }
    )