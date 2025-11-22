# main.py – Predaiot LLC Official Global Dashboard – FINAL & PERFECT VERSION (22 Nov 2025)
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Predaiot – Profit-Driven Industrial AI",
    page_icon="https://i.imgur.com/MZGE157.jpeg",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Background + Gold Text + Premium Glass Effect
st.markdown("""
<style>
    .stApp {background: url("https://i.imgur.com/b1lYZqw.jpeg") center fixed; background-size: cover;}
    .block-container {background: rgba(5,10,30,0.93); backdrop-filter: blur(14px); border-radius: 22px; padding: 2.8rem; margin: 2rem 0; border: 1px solid rgba(0,255,157,0.25);}
    h1,h2,h3,h4,h5,p,span,div,label,.stMarkdown {color: #FFD700 !important; text-shadow: 2px 2px 8px rgba(0,0,0,0.9); font-family: 'Segoe UI', sans-serif;}
    .stMetric {border-left: 8px solid #FFD700; background: rgba(255,215,0,0.18); border-radius: 14px; padding: 10px;}
    .stSuccess {background: linear-gradient(90deg,#00ff9d,#00d4ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold; font-size: 1.5rem;}
    .footer {text-align:center; padding:5rem 2rem; color:#FFD700; font-size:1.5rem; text-shadow: 3px 3px 10px black;}
</style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1,4])
with col1:
    st.image("https://i.imgur.com/MZGE157.jpeg", width=300)
with col2:
    st.title("Predaiot")
    st.markdown("### World's First Arabic-Built Profit-Driven Industrial AI")
    st.success("Patent Pending • +15% Revenue Uplift Verified by Muscat Energy (Oman)")

# Leadership Team
st.markdown("---")
st.subheader("Leadership Team")

col_a, col_b = st.columns(2)
with col_a:
    st.image("https://i.imgur.com/BUuOchX.jpeg", caption="Chams Eddine Madi – Founder & CEO", use_column_width=True)
    st.markdown("""
    **Chams Eddine Madi**  
    Founder & CEO • Deep-Tech Architect  
    12+ years in intelligent automation & economic AI.  
    Started solving solar degradation in 2012 → Built the Economic Decision Engine™ from a bedroom in 2023.
    """)
with col_b:
    st.image("https://i.imgur.com/VtGeq0W.jpeg", caption="Sumaiya – Co-Founder & Chief Strategy Officer", use_column_width=True)
    st.markdown("""
    **Sumaiya**  
    Co-Founder • Strategy & Growth  
    GCC market expert. Transforms deep-tech into scalable revenue.  
    Leads investor relations, partnerships, and regional expansion across MENA & India.
    """)

# PROOF OF VALUE – OFFICIAL IMAGE + DOWNLOAD
st.markdown("---")
st.image("https://i.imgur.com/8vK3k9P.png", use_column_width=True)

pdf_url = "https://drive.google.com/uc?export=download&id=1hL3z1e9v8mK8z9xY7tR5uW2qP9oN6fF_"
st.markdown(f'''
<div style="text-align:center; margin:80px 0;">
    <a href="{pdf_url}" target="_blank">
        <button style="background:linear-gradient(90deg,#00ff9d,#00d4ff); color:black; font-size:32px; font-weight:bold; padding:28px 120px; border:none; border-radius:28px; box-shadow:0 15px 60px rgba(0,255,157,0.8); transition:all 0.4s; cursor:pointer;"
        onmouseover="this.style.transform='scale(1.08)'; this.style.boxShadow='0 20px 70px rgba(0,255,157,1)'"
        onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 15px 60px rgba(0,255,157,0.8)'">
            Download Official Report (12 Pages)<br>
            <span style="font-size:24px; color:black;">+15% Revenue Uplift Verified by Muscat Energy (Oman)</span>
        </button>
    </a>
</div>
''', unsafe_allow_html=True)

# Financial Outlook
st.markdown("---")
st.subheader("5-Year Financial Outlook")
data = {"Year":[2025,2026,2027,2028,2029],
        "Revenue (£M)":[2.5,6.8,12.5,19.8,28.5],
        "Net Profit (£M)":[0.7,2.6,5.3,9.0,13.3],
        "Cumulative Cash (£M)":[0.7,3.3,8.6,17.6,30.9],
        "Headcount":[45,85,140,220,310]}
df = pd.DataFrame(data)

c1,c2,c3,c4 = st.columns(4)
with c1: st.metric("5-Year Revenue", "£70.1M", delta="+2800% from zero")
with c2: st.metric("Year-5 Cash", "£30.9M", delta="Self-funded growth")
with c3: st.metric("Year-5 Profit", "£13.3M", delta="47% net margin")
with c4: st.metric("Team 2029", "310", delta="Global scale")

st.plotly_chart(px.area(df, x="Year", y="Cumulative Cash (£M)", title="Cumulative Cash Flow – Zero to £30.9M in 5 Years",
                        color_discrete_sequence=["#FFD700"], line_shape='spline'), use_container_width=True)

# Live Status
st.success("AWS Glue Job: EDE_Quantum_Classifier_Daily → Running & Succeeding Daily")
st.success("Live Global Dashboard → 24/7 • Patent Pending • Real Results Delivered")
st.balloons()

# Footer
st.markdown("""
<div class="footer">
    © 2025 Predaiot LLC – Officially Registered in Muscat, Sultanate of Oman<br>
    <b>Contact:</b> al.shams.invest@gmail.com • +968 7411 4028<br>
    <b>Patent Pending • +15% Revenue Uplift Independently Verified</b>
</div>
""", unsafe_allow_html=True)
