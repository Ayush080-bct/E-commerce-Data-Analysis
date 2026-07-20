import plotly.express as px
import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
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
 
if st.button("Predict Segment", type="primary"):
    result = call_predict(recency, frequency, monetary)
    st.success(
        f"**Predicted Cluster:** {result['cluster']}  \n"
        f"**Likely Segment:** {result['segment']}"
    )
 
    st.markdown("#### How this compares to existing customers")
    fig = px.scatter(
        scatter_df, x="Frequency", y="Monetory", color=scatter_df["Cluster"].astype(str),
        opacity=0.35,
    )
    fig.add_scatter(
        x=[frequency], y=[monetary],
        mode="markers", marker=dict(size=18, color="red", symbol="star"),
        name="New customer",
    )
    st.plotly_chart(fig, width='stretch')