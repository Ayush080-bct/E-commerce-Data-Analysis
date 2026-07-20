
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
import plotly.express as px
import streamlit as st

from api_client import fetch_customer, fetch_customer_ids, fetch_scatter_df, require_backend

st.set_page_config(page_title="Customer Lookup", page_icon="🔍", layout="wide")
require_backend()

st.title("Customer Lookup")

ids = fetch_customer_ids()
selected_id = st.selectbox("Search by Customer ID", options=ids)

if selected_id:
    customer = fetch_customer(selected_id)
    if customer is None:
        st.warning("Customer not found.")
    else:
        st.markdown("---")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Recency (days)", int(customer["Recency"]))
        c2.metric("Frequency (orders)", int(customer["Frequency"]))
        c3.metric("Monetary (£)", f"{customer['Monetory']:,.2f}")
        c4.metric("RFM Score", customer["RFM_score"])

        c5, c6 = st.columns(2)
        c5.info(f"**Rule-based segment:** {customer['segment']}")
        c6.info(
            f"**KMeans cluster:** {customer['cluster']} "
            f"(typically '{customer['cluster_typical_segment']}')"
        )

        st.markdown("#### Where this customer sits vs. everyone else")
        scatter_df = fetch_scatter_df()
        fig = px.scatter(
            scatter_df, x="Frequency", y="Monetory", color=scatter_df["Cluster"].astype(str),
            opacity=0.4,
        )
        fig.add_scatter(
            x=[customer["Frequency"]], y=[customer["Monetory"]],
            mode="markers", marker=dict(size=16, color="black", symbol="star"),
            name="This customer",
        )
        st.plotly_chart(fig, width='stretch')