"""
Customer Segementation Dashboard - entry point
Run : streamlit run dashboard/app.py
Actual pages live in dashboard/pages/ and are auto-detected by streamlit
"""
import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from api_client import API_BASE_URL , require_backend

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide"
)

