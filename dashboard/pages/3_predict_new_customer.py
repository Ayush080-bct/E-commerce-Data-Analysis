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

scatter_df = fetch_scatter_df()
r_min, r_max = int(scatter_df["Recency"].min()), int(scatter_df["Recency"].max())
f_min, f_max = int(scatter_df["Frequency"].min()), int(scatter_df["Frequency"].max())
m_min, m_max = float(scatter_df["Monetory"].min()), float(scatter_df["Monetory"].max())

c1, c2, c3 = st.columns(3)
recency = c1.slider("Recency (days since last purchase)", r_min, r_max, int(scatter_df["Recency"].median()))
frequency = c2.slider("Frequency (number of orders)", f_min, f_max, int(scatter_df["Frequency"].median()))
monetary = c3.slider("Monetary (total spend, £)", m_min, m_max, float(scatter_df["Monetory"].median()))
