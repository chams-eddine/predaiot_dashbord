# main.py – Predaiot LLC Official Global Website (22 Nov 2025)
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Predaiot – Profit-Driven Industrial AI", page_icon="https://i.imgur.com/MZGE157.jpeg", layout="wide")

# Full Background + Gold Text
st.markdown("""
<style>
    .stApp {background: url("https://i.imgur.com/b1lYZqw.jpeg") center fixed; background-size: cover;}
    .block-container {background: rgba(5,10,30,0.92); backdrop-filter: blur(12px); border-radius: 20px; padding: 2rem; margin: 1.5rem 0;}
    h1,h2,h3,h4,p,span,div,label {color: #FFD700 !important; text-shadow: 2px 2px 6px rgba(0,0,0,0.9);}
    .stMetric {border-left: 6px solid #FFD700; background: rgba(255,215,0,0.15);}
    .footer {text-align:center; padding:3rem; color:#FFD700; font-size:1.3rem;}
</style>
""", unsafe_allow_html=True)

# Hero Section
col1, col2 = st.columns([1,2])
with col1:
    st.image("https://i.imgur.com/MZGE157.jpeg", width=280)
with col2:
    st.title("Predaiot")
    st.markdown("### Profit-Driven Industrial Intelligence")
    st.success("Patent Pending • +15% Revenue Uplift Verified by Muscat Energy (Oman)")

# Team Section
st.markdown("---")
st.subheader("Leadership")
col_a, col_b = st.columns(2)
with col_a:
    st.image("https://i.imgur.com/YOUR_CHAMS_PHOTO_DIRECT_LINK.jpeg", width=300, caption="Chams Eddine Madi – Founder & CEO")
    st.markdown("""
    **Chams Eddine Madi**  
    Founder & CEO • Systems Architect  
    10+ years building real-time profit-optimization engines.  
    Started solving solar degradation problems in 2012 → created the Economic Decision Engine™ in 2023.
    """)
with col_b:
    st.image("https://i.imgur.com/YOUR_SUMAIYA_PHOTO_DIRECT_LINK.jpeg", width=300, caption="Sumaiya – Co-Founder & Strategy")
    st.markdown("""
    **Sumaiya**  
    Co-Founder • Strategy & Growth  
    GCC market specialist. Turns deep-tech into commercial reality.  
    Leads investor relations, partnerships, and regional expansion.
    """)

# Proof of Value
st.markdown("---")
st.image("https://i.imgur.com/8vK3k9P.png", use_column_width=True)
pdf_url = "https://drive.google.com/uc?export=download&id=1hL3z1e9v8mK8z9xY7tR5uW2qP9oN6fF_"
st.markdown(f'''
<div style="text-align:center; margin:60px 0;">
    <a href="{pdf_url}" target="_blank">
        <button style="background:linear-gradient(90deg,#00ff9d,#00d4ff); color:black; font-size:28px; font-weight:bold; padding:22px 90px; border:none; border-radius:20px; box-shadow:0 12px 40px rgba(0,255,157,0.6);">
            Download Official Report<br><span style="font-size:20px;">+15% Revenue Uplift Verified by Muscat Energy</span>
        </button>
    </a>
</div>
''', unsafe_allow_html=True)

# Financial Snapshot
st.markdown("---")
st.subheader("5-Year Financial Outlook")
data = {"Year":[2025,2026,2027,2028,2029],"Revenue (£M)":[2.5,6.8,12.5,19.8,28.5],"Cumulative Cash (£M)":[0.7,3.3,8.6,17.6,30.9]}
df = pd.DataFrame(data)
c1,c2,c3,c4 = st.columns(4)
with c1: st.metric("5-Year Revenue", "£70.1M")
with c2: st.metric("Year-5 Cash", "£30.9M")
with c3: st.metric("Year-5 Profit", "£13.3M")
with c4: st.metric("Team 2029", "310")
st.plotly_chart(px.area(df, x="Year", y="Cumulative Cash (£M)", color_discrete_sequence=["#FFD700"]), use_container_width=True)

# Footer
st.markdown("""
<div class="footer">
    © 2025 Predaiot LLC – Registered in Muscat, Sultanate of Oman<br>
    al.shams.invest@gmail.com • +968 7411 4028 • Patent Pending
</div>
""", unsafe_allow_html=True)
st.balloons()
