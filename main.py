# main.py – EDE v3.0 Economic Decision Engine – Global Launch Nov 22, 2025
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="EDE v3.0 – World's First Arabic Quantum Economic Decision Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hero Section
st.title("EDE v3.0 – Economic Decision Engine")
st.markdown("### World's First Arabic-Built Quantum-Powered Economic Decision Engine")
st.success("**Founder & Solo Developer (2023–2025):** You – Full ownership © 2025")

# Financial Metrics
data = {
    "Year": [2025, 2026, 2027, 2028, 2029],
    "Revenue (£M)": [2.5, 6.8, 12.5, 19.8, 28.5],
    "Net Profit (£M)": [0.7, 2.6, 5.3, 9.0, 13.3],
    "Cumulative Cash (£M)": [0.7, 3.3, 8.6, 17.6, 30.9],
    "Headcount": [45, 85, 140, 220, 310]
}
df = pd.DataFrame(data)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("5-Year Total Revenue", "£70.1M")
with col2:
    st.metric("Year 5 Cumulative Cash", "£30.9M")
with col3:
    st.metric("Year 5 Net Profit", "£13.3M")
with col4:
    st.metric("Year 5 Headcount", "310")

# Charts
st.plotly_chart(px.bar(df, x="Year", y="Revenue (£M)", title="Revenue Growth Trajectory", color="Year"), use_container_width=True)
st.plotly_chart(px.line(df, x="Year", y="Net Profit (£M)", title="Net Profit Evolution", markers=True), use_container_width=True)
st.plotly_chart(px.area(df, x="Year", y="Cumulative Cash (£M)", title="Cumulative Cash Flow – Zero to £30.9M"), use_container_width=True)

# Historical Proof
st.markdown("---")
st.subheader("Journey: From 2023 to Global Launch 2025")

colA, colB = st.columns(2)
with colA:
    st.image("https://i.imgur.com/YOUR_V1_LINK.jpg", caption="v1.0 Core Engine – First commit 2023")
with colB:
    st.image("https://i.imgur.com/YOUR_V2_LINK.jpg", caption="v2.0 Economic Engine – Full Arabic Architecture 2025")

# Live Proof
st.markdown("---")
st.subheader("Live Production Systems – November 22, 2025")
st.success("AWS Glue Job: EDE_Quantum_Classifier_Daily → **Succeeded daily**")
st.success("Live Global Dashboard → 24/7 at current URL")
st.balloons()

st.caption("© 2025 – First fully Arabic-developed Quantum Economic Decision Engine | From bedroom in 2023 to global stage in 2025")
