import plotly.express as px
import streamlit as st
 
from api_client import fetch_customer, fetch_customer_ids, fetch_scatter_df, require_backend
 
st.set_page_config(page_title="Customer Lookup", page_icon="🔍", layout="wide")
require_backend()
 
st.title("Customer Lookup")
 
ids = fetch_customer_ids()
selected_id = st.selectbox("Search by Customer ID", options=ids)
 
 