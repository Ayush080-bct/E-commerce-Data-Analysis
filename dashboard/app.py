
"""
Customer Segmentation Dashboard — entry point.
Run: streamlit run dashboard/app.py
Actual pages live in dashboard/pages/ and are auto-detected by Streamlit.
"""
 
import streamlit as st
 
from api_client import API_BASE_URL, require_backend
 
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide",
)
 
require_backend()
 
st.sidebar.title("📊 Segmentation Dashboard")
st.sidebar.caption(f"Backend: {API_BASE_URL}")
 
st.title("Customer Segmentation Dashboard")
st.write(
    "An interactive view of the RFM segmentation and KMeans clustering "
    "results from the analysis notebooks — backed by a FastAPI service."
)

 
st.markdown("### Pages")
c1, c2, c3 = st.columns(3)
