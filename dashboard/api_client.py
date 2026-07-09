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
    r = requests.get(f"{API_BASE_URL}",timeout=10,**kwargs)
    r.raise_for_status()
    return r.json()

def _post(path:str,json_body:dict):
    """ Send a POST request to the backend with a JSON body and return the JSON response."""
    r = requests.post(f"{API_BASE_URL}",json=json_body,timeout=10)
    r.raise_for_status()
    return r.json()

# Unlike TypeScript, Python does not enforce type safety at compile time.
# Therefore, we use generic helper functions (_get and _post) to centralize
# request logic, error handling, and JSON parsing. Streamlit pages import
# this module to fetch/submit data without duplicating request code.

