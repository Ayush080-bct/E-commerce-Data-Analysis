import pandas as pd
import plotly.express as px
import streamlit as st

from api_client import fetch_overview, fetch_scatter_df, require_backend

st.set_page_config(page_title="Overview", page_icon="📈", layout="wide")
require_backend()

st.title("Customer Segmentation Overview")

overview = fetch_overview()
scatter_df = fetch_scatter_df()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", f"{overview['total_customers']:,}")
col2.metric("Total Revenue", f"£{overview['total_revenue']:,.0f}")
col3.metric("Avg. Order Value", f"£{overview['avg_order_value']:,.2f}")
col4.metric("Segments", overview["num_segments"])

st.markdown("---")
c1, c2 = st.columns(2)

with c1:
    st.subheader("Customers by Segment")
    seg_counts = pd.DataFrame(
        list(overview["segment_counts"].items()), columns=["segment", "count"]
    )
    fig = px.bar(seg_counts, x="segment", y="count", color="segment", text="count")
    fig.update_layout(showlegend=False, xaxis_title="", yaxis_title="Customers")
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("Revenue by Segment")
    rev = pd.DataFrame(
        list(overview["revenue_by_segment"].items()), columns=["segment", "revenue"]
    )
    fig = px.pie(rev, names="segment", values="revenue", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
c3, c4 = st.columns(2)

with c3:
    st.subheader("RFM Clusters (KMeans)")
    fig = px.scatter(
        scatter_df, x="Frequency", y="Monetory", color=scatter_df["Cluster"].astype(str),
        hover_data=["CustomerID", "Recency", "segment"],
        labels={"color": "Cluster"},
    )
    st.plotly_chart(fig, use_container_width=True)

with c4:
    st.subheader("Recency Distribution")
    fig = px.histogram(scatter_df, x="Recency", nbins=30, color="segment")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Segment Summary")
summary_df = pd.DataFrame(overview["summary"]).sort_values("Avg_Monetary", ascending=False)
st.dataframe(summary_df, use_container_width=True)