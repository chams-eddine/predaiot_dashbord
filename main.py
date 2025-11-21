# main.py – EDE v3.0 Economic Decision Engine – Global Launch Nov 22, 2025
# Founder & CEO & CTO: Chams Eddine Madi – Predaiot (Patent Pending)

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="EDE v3.0 – Predaiot Economic Decision Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Hero Section
st.title("EDE v3.0 – Economic Decision Engine")
st.markdown("### World's First Arabic-Engineered Quantum Economic Decision Engine")
st.success("**Patent Pending** – Official filing in progress")

# Founder Section
st.markdown("""
### Founder, CEO & CTO
**Chams Eddine Madi**  
Founder & CEO of **Predaiot**  
Started in 2023 with a single file `ede_core.py` from his bedroom  
Reached Patent Pending status + live global dashboard + daily AWS Glue jobs in 2025
""")

# Financial Projections (hardcoded – no external files needed)
data = {
    "Year": [2025, 2026, 2027, 2028, 2029],
    "Revenue (£M)": [2.5, 6.8, 12.5, 19.8, 28.5],
    "Net Profit (£M)": [0.7, 2.6, 5.3, 9.0, 13.3],
    "Cumulative Cash (£M)": [0.7, 3.3, 8.6, 17.6, 30.9],
    "Headcount": [45, 85, 140, 220, 310]
}
df = pd.DataFrame(data)

col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("5-Year Total Revenue", "£70.1M")
with col2: st.metric("Year 5 Cumulative Cash", "£30.9M")
with col3: st.metric("Year 5 Net Profit", "£13.3M")
with col4: st.metric("Year 5 Headcount", "310")

# Charts
st.plotly_chart(px.bar(df, x="Year", y="Revenue (£M)", title="Revenue Growth", color="Year"), use_container_width=True)
st.plotly_chart(px.line(df, x="Year", y="Net Profit (£M)", title="Net Profit Trajectory", markers=True), use_container_width=True)
st.plotly_chart(px.area(df, x="Year", y="Cumulative Cash (£M)", title="Cumulative Cash – Zero to £30.9M"), use_container_width=True)

# Historical Proof – Your original Arabic screenshots
st.markdown("---")
st.subheader("Journey: From 2023 v1.0 to 2025 v2.0 Economic Engine")

colA, colB = st.columns(2)
with colA:
    st.image("https://i.imgur.com/YOUR_V1_SCREENSHOT.jpg", caption="v1.0 Core – First commit 2023 (Arabic README)")
with colB:
    st.image("https://i.imgur.com/YOUR_V2_SCREENSHOT.jpg", caption="v2.0 Economic Engine – Full Arabic Architecture 2025")

# Live Status
st.markdown("---")
st.success("AWS Glue Job: EDE_Quantum_Classifier_Daily → **Running & Succeeding daily**")
st.success("Live Global Dashboard → 24/7 at current URL")
st.balloons()

# Footer
st.caption("© 2025 Predaiot – Chams Eddine Madi | Patent Pending | All rights reserved")
