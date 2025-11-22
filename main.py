# main.py – Predaiot EDE v3.0 – Official Global Dashboard with Full Background
# Predaiot LLC – Registered in Muscat, Sultanate of Oman
# Founder & CEO: Chams Eddine Madi – Patent Pending

import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Predaiot – EDE v3.0",
    page_icon="https://i.imgur.com/MZGE157.jpeg",
    layout="wide"
)

# خلفية كاملة + تظليل أنيق (الصورة اللي بعتها)
page_bg_img = '''
<style>
    .stApp {
        background: url("https://i.imgur.com/b1lYZqw.jpeg") no-repeat center center fixed;
        background-size: cover;
    }
    /* تظليل خفيف عشان النصوص تبان بوضوح */
    .css-1d391kg > div, .css-1v0mbdj, .block-container {
        background: rgba(10, 14, 31, 0.88) !important;
        backdrop-filter: blur(8px);
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
    }
    h1, h2, h3 {color: #00ff9d !important;}
    .stMetric > div {border-left: 6px solid #00ff9d; background: rgba(0,255,157,0.15);}
    .footer {text-align: center; padding: 3rem; color: #00d4ff; font-size: 1.2rem;}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Header + Logo
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://i.imgur.com/MZGE157.jpeg", width=220)
with col2:
    st.title("Predaiot – EDE v3.0")
    st.markdown("### World's First Arabic-Built Quantum Economic Decision Engine")
    st.success("Patent Pending – Official Filing in Progress")

# Founder & Company
st.markdown("""
**Chams Eddine Madi**  
Founder & CEO • Predaiot LLC  
Registered in Muscat, Sultanate of Oman  
Email: al.shams.invest@gmail.com • Phone: +968 7411 4028
""")

# Financial Metrics
data = {"Year": [2025,2026,2027,2028,2029],
        "Revenue (£M)": [2.5,6.8,12.5,19.8,28.5],
        "Net Profit (£M)": [0.7,2.6,5.3,9.0,13.3],
        "Cumulative Cash (£M)": [0.7,3.3,8.6,17.6,30.9],
        "Headcount": [45,85,140,220,310]}
df = pd.DataFrame(data)

c1,c2,c3,c4 = st.columns(4)
with c1: st.metric("5-Year Revenue", "£70.1M")
with c2: st.metric("Year 5 Cash", "£30.9M")
with c3: st.metric("Year 5 Profit", "£13.3M")
with c4: st.metric("Team 2029", "310")

# Charts
st.plotly_chart(px.area(df, x="Year", y="Cumulative Cash (£M)", title="Cumulative Cash – Zero to £30.9M",
                        color_discrete_sequence=["#00ff9d"]), use_container_width=True)
st.plotly_chart(px.bar(df, x="Year", y="Revenue (£M)", title="Revenue Growth",
                       color_discrete_sequence=px.colors.sequential.Plasma_r), use_container_width=True)

# Journey Section
st.markdown("---")
st.subheader("From Bedroom 2023 → Global Company 2025")

colA, colB = st.columns(2)
with colA:
    st.image("https://i.imgur.com/2ujGoG4.png", caption="v1.0 – First Arabic Core 2023")
    st.image("https://i.imgur.com/4P5Q48d.png", caption="Project Structure")
with colB:
    st.image("https://i.imgur.com/dzQsCaZ.png", caption="v2.0 Economic Engine 2025")
    st.image("https://i.imgur.com/BvHPeYs.png", caption="Microservices + Graph Architecture")

st.image("https://i.imgur.com/eCyISer.png", caption="v2.0 Detailed View", use_column_width=True)
st.image("https://i.imgur.com/H52AhVg.png", caption="Live Execution & Testing", use_column_width=True)

# Live Status
st.success("AWS Glue Job → Running & Succeeding daily")
st.success("Live Global Dashboard → 24/7 – Patent Pending")
st.balloons()

# Footer
st.markdown("""
<div class="footer">
    © 2025 Predaiot LLC – Muscat, Sultanate of Oman<br>
    Contact: al.shams.invest@gmail.com • +968 7411 4028<br>
    <b>Patent Pending • All rights reserved</b>
</div>
""", unsafe_allow_html=True)
