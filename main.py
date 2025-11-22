# main.py – Predaiot EDE v3.0 – Official Global Dashboard
# Registered Company: Predaiot LLC, Muscat, Sultanate of Oman
# Founder & CEO: Chams Eddine Madi

import streamlit as st
import pandas as pd
import plotly.express as px

# ====================== PAGE CONFIG & CUSTOM CSS ======================
st.set_page_config(
    page_title="Predaiot – EDE v3.0 Economic Decision Engine",
    page_icon="https://i.imgur.com/YOUR_LOGO_LINK.png",  # حط رابط اللوقو هنا بعد الرفع
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS – ألوان Predaiot الرسمية (نفس اللوقو)
st.markdown("""
<style>
    .css-1d391kg {background: #0a1a2f;}  /* Dark navy background */
    .css-1v0mbdj {color: #00ff9d !important;} /* Accent green */
    .stMetric > div {background: rgba(10,26,47,0.8); border-left: 5px solid #00ff9d;}
    .stSuccess {background: linear-gradient(90deg, #00ff9d, #00d4ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
    .footer {text-align: center; padding: 2rem; background: #0a1a2f; color: #00d4ff; font-size: 1rem;}
</style>
""", unsafe_allow_html=True)

# ====================== HEADER WITH LOGO ======================
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://i.imgur.com/YOUR_PREDAIOT_LOGO.png", width=180)  # ارفع اللوقو على imgur وحط الرابط هنا
with col2:
    st.title("Predaiot – EDE v3.0")
    st.markdown("### World's First Arabic Quantum Economic Decision Engine")
    st.success("**Patent Pending** – Official filing in progress")

# ====================== FOUNDER & COMPANY INFO ======================
st.markdown(f"""
**Chams Eddine Madi**  
Founder & CEO • Predaiot LLC  
Registered in Muscat, Sultanate of Oman  
Email: al.shams.invest@gmail.com | Phone: +968 7411 4028
""")

# ====================== FINANCIAL METRICS ======================
data = {
    "Year": [2025, 2026, 2027, 2028, 2029],
    "Revenue (£M)": [2.5, 6.8, 12.5, 19.8, 28.5],
    "Net Profit (£M)": [0.7, 2.6, 5.3, 9.0, 13.3],
    "Cumulative Cash (£M)": [0.7, 3.3, 8.6, 17.6, 30.9],
    "Headcount": [45, 85, 140, 220, 310]
}
df = pd.DataFrame(data)

c1, c2, c3, c4 = st.columns(4)
with c1: st.metric("5-Year Revenue", "£70.1M")
with c2: st.metric("Year 5 Cash", "£30.9M")
with c3: st.metric("Year 5 Profit", "£13.3M")
with c4: st.metric("Team Size (2029)", "310")

# ====================== CHARTS ======================
st.plotly_chart(px.area(df, x="Year", y="Cumulative Cash (£M)", 
                        title="Cumulative Cash Flow – Zero to £30.9M", 
                        color_discrete_sequence=["#00ff9d"]), use_container_width=True)

st.plotly_chart(px.bar(df, x="Year", y="Revenue (£M)", 
                       title="Revenue Growth", color="Year",
                       color_discrete_sequence=px.colors.sequential.Plasma_r), use_container_width=True)

# ====================== HISTORICAL PROOF ======================
st.markdown("---")
st.subheader("Journey: From 2023 to 2025")
colA, colB = st.columns(2)
with colA:
    st.image("https://i.imgur.com/v1_screenshot.jpg", caption="v1.0 – First commit 2023 (Arabic)")
with colB:
    st.image("https://i.imgur.com/v2_screenshot.jpg", caption="v2.0 Economic Engine – Full Arabic Architecture 2025")

# ====================== LIVE STATUS ======================
st.success("AWS Glue Job: EDE_Quantum_Classifier_Daily → Running daily")
st.success("Live Global Dashboard → 24/7")

# ====================== FOOTER ======================
st.markdown(f"""
<div class="footer">
    © 2025 Predaiot LLC • Registered in Muscat, Sultanate of Oman • Patent Pending<br>
    <b>Contact:</b> al.shams.invest@gmail.com • +968 7411 4028
</div>
""", unsafe_allow_html=True)

st.balloons()
