import plotly.express as px
import streamlit as st

from api_client import call_predict, fetch_scatter_df, require_backend

st.set_page_config(page_title="Predict New Customer", page_icon="🔮", layout="wide")
require_backend()

st.title("Predict Segment for a New / Hypothetical Customer")
st.write(
    "Move the sliders to describe a customer's purchase behavior and see "
    "which cluster and segment they'd fall into — prediction runs through "
    "the FastAPI `/predict` endpoint."
)