"""
Customer Segmentation Dashboard — entry point.
Run: streamlit run dashboard/app.py
Actual pages live in dashboard/pages/ and are auto-detected by Streamlit.
"""

import streamlit as st

from api_client import API_BASE_URL, fetch_overview, require_backend

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide",
)

require_backend()

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
st.sidebar.title("📊 Segmentation Dashboard")
st.sidebar.caption(f"Backend: `{API_BASE_URL}`")
st.sidebar.success("Backend connected", icon="🟢")

# ---------------------------------------------------------------------------
# Hero section
# ---------------------------------------------------------------------------
st.title("Customer Segmentation Dashboard")
st.caption(
    "An interactive view of the RFM segmentation and KMeans clustering "
    "results from the analysis notebooks — backed by a FastAPI service."
)

st.write("")  # small breathing room

# ---------------------------------------------------------------------------
# At-a-glance stats (pulls the same /overview data the Overview page uses,
# so this page earns its place instead of being an empty landing screen)
# ---------------------------------------------------------------------------
overview = fetch_overview()

m1, m2, m3, m4 = st.columns(4)
m1.metric("Customers", f"{overview['total_customers']:,}")
m2.metric("Total Revenue", f"£{overview['total_revenue']:,.0f}")
m3.metric("Avg. Order Value", f"£{overview['avg_order_value']:,.2f}")
m4.metric("Segments", overview["num_segments"])

st.divider()

# ---------------------------------------------------------------------------
# Page cards
# ---------------------------------------------------------------------------
st.subheader("Explore")

cards = [
    {
        "icon": "📈",
        "title": "Overview",
        "desc": "Segment counts, revenue split, and cluster visualization.",
        "page": "pages/1_overview.py",
        "label": "Open Overview",
    },
    {
        "icon": "🔍",
        "title": "Customer Lookup",
        "desc": "Look up any customer's RFM values, score, and cluster.",
        "page": "pages/2_customer_lookup.py",
        "label": "Open Customer Lookup",
    },
    {
        "icon": "🔮",
        "title": "Predict New Customer",
        "desc": "Enter hypothetical RFM values and predict the segment live.",
        "page": "pages/3_predict_new_customer.py",
        "label": "Open Prediction",
    },
]

cols = st.columns(3)
for col, card in zip(cols, cards):
    with col:
        with st.container(border=True):
            st.markdown(f"### {card['icon']} {card['title']}")
            st.write(card["desc"])
            st.page_link(card["page"], label=card["label"], icon=card["icon"])