# main.py – Predaiot LLC Official Global Website – Final Version 22 Nov 2025
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Predaiot – Profit-Driven Industrial AI",
    page_icon="https://i.imgur.com/MZGE157.jpeg",
    layout="wide"
)

# Full Background + Gold Text + Glass Effect
st.markdown("""
<style>
    .stApp {background: url("https://i.imgur.com/b1lYZqw.jpeg") center fixed; background-size: cover;}
    .block-container {background: rgba(5,10,30,0.92); backdrop-filter: blur(12px); border-radius: 20px; padding: 2.5rem; margin: 1.5rem 0; border: 1px solid rgba(0,255,157,0.2);}
    h1,h2,h3,h4,p,span,div,label,.stMarkdown {color: #FFD700 !important; text-shadow: 2px 2px 6px rgba(0,0,0,0.9); font-weight: 600;}
    .stMetric {border-left: 8px solid #FFD700; background: rgba(255,215,0,0.15); border-radius: 12px;}
    .stSuccess {background: linear-gradient(90deg,#00ff9d,#00d4ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold; font-size: 1.4rem;}
    .footer {text-align:center; padding:4rem; color:#FFD700; font-size:1.4rem; text-shadow: 2px 2px 8px black;}
</style>
""", unsafe_allow_html=True)

# Hero Section
col1, col2 = st.columns([1,3])
with col1:
    st.image("https://i.imgur.com/MZGE157.jpeg", width=280)
with col2:
    st.title("Predaiot")
    st.markdown("### Profit-Driven Industrial Intelligence")
    st.success("Patent Pending • +15% Revenue Uplift Verified by Muscat Energy (Oman)")

# Leadership Team
st.markdown("---")
st.subheader("Leadership")
col_a, col_b = st.columns(2)
with col_a:
    st.image("https://i.imgur.com/BUuOchX.jpeg", caption="Chams Eddine Madi – Founder & CEO", use_column_width=True)
    st.markdown("""
    **Chams Eddine Madi**  
    Founder & CEO • Systems Architect  
    10+ years building real-time profit-optimization engines.  
    Started solving solar degradation in 2012 → created the Economic Decision Engine™.
    """)
with col_b:
    st.image("https://i.imgur.com/VtGeq0W.jpeg", caption="Sumaiya – Co-Founder & Strategy", use_column_width=True)
    st.markdown("""
    **Sumaiya**  
    Co-Founder • Strategy & Growth  
    GCC market specialist. Turns deep-tech into commercial reality.  
    Leads investor relations, partnerships, and regional expansion.
    """)

# Proof of Value – Official Image + Download Button
st.markdown("---")
st.image("https://i.imgur.com/8vK3k9P.png", use_column_width=True)

pdf_url = "https://drive.google.com/uc?export=download&id=1hL3z1e9v8mK8z9xY7tR5uW2qP9oN6fF_"
st.markdown(f'''
<div style="text-align:center; margin:70px 0;">
    <a href="{pdf_url}" target="_blank">
        <button style="background:linear-gradient(90deg,#00ff9d,#00d4ff); color:black; font-size:30px; font-weight:bold; padding:25px 100px; border:none; border-radius:24px; box-shadow:0 15px 50px rgba(0,255,157,0.7); transition:all 0.4s;"
        onmouseover="this.style.transform='scale(1.08)'" onmouseout="this.style.transform='scale(1)'">
            Download Official 12-Page Report<br>
            <span style="font-size:22px;">+15% Revenue Uplift Verified by Muscat Energy (Oman)</span>
        </button>
    </a>
</div>
''', unsafe_allow_html=True)

# Financial Snapshot
st.markdown("---")
st.subheader("5-Year Financial Outlook")
data = {"Year":[2025,2026,2027,2028,2029],
        "Revenue (£M)":[2.5,6.8,12.5,19.8,28.5],
        "Net Profit (£M)":[0.7,2.6,5.3,9.0,13.3],
        "Cumulative Cash (£M)":[0.7,3.3,8.6,17.6,30.9]}
df = pd.DataFrame(data)

c1,c2,c3,c4 = st.columns(4)
with c1: st.metric("5-Year Revenue", "£70.1M")
with c2: st.metric("Year-5 Cash", "£30.9M")
with c3: st.metric("Year-5 Profit", "£13.3M")
with c4: st.metric("Team 2029", "310")

st.plotly_chart(px.area(df, x="Year", y="Cumulative Cash (£M)", title="Cumulative Cash – Zero to £30.9M",
                        color_discrete_sequence=["#FFD700"]), use_container_width=True)

# Live Status
st.success("AWS Glue Job Running Daily • Live Dashboard 24/7 • Patent Pending")
st.balloons()

# Footer
st.markdown("""
<div class="footer">
    © 2025 Predaiot LLC – Registered in Muscat, Sultanate of Oman<br>
    Contact: al.shams.invest@gmail.com • +968 7411 4028<br>
    <b>Patent Pending • +15% Revenue Uplift Verified</b>
</div>
""", unsafe_allow_html=True)
