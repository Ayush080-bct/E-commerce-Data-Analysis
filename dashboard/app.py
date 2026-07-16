
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
 
with c1:
    st.markdown("#### 📈 Overview")
    st.write("Segment counts, revenue split, and cluster visualization.")
    st.page_link("pages/1_overview.py", label="Go to Overview", icon="📈")
 

with c2:
    st.markdown("#### 🔍 Customer Lookup")
    st.write("Look up any customer's RFM values, score, and cluster.")
    st.page_link("pages/2_customer_lookup.py", label="Go to Customer Lookup", icon="🔍")
 
with c3:
    st.markdown("#### 🔮 Predict New Customer")
    st.write("Enter hypothetical RFM values and predict the segment live.")
    st.page_link("pages/3_predict_new_customer.py", label="Go to Prediction", icon="🔮")