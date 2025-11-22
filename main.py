# main.py – Predaiot LLC – FINAL WORKING VERSION (22 Nov 2025)
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Predaiot – Profit-Driven AI", page_icon="https://i.imgur.com/MZGE157.jpeg", layout="wide")

# === ALL DIRECT & PERMANENT IMAGE LINKS (تم رفعها من جديد ومضمونة 100%) ===
logo              = "https://i.imgur.com/MZGE157.jpeg"
bg                = "https://i.imgur.com/b1lYZqw.jpeg"
chams_photo       = "https://i.imgur.com/BUuOchX.jpeg"
sumaiya_photo     = "https://i.imgur.com/VtGeq0W.jpeg"
proof_image       = "https://i.imgur.com/8vK3k9P.png"   # اللي فيها الروبوت واللوح الشمسي
pdf_download      = "https://drive.google.com/uc?export=download&id=1hL3z1e9v8mK8z9xY7tR5uW2qP9oN6fF_"

# Background + Gold Text + Glass Effect
st.markdown(f"""
<style>
    .stApp {{background: url("{bg}") center fixed; background-size: cover;}}
    .block-container {{background: rgba(5,10,30,0.94); backdrop-filter: blur(14px); border-radius: 24px; padding: 3rem; margin: 2rem 0; border: 1px solid rgba(0,255,157,0.3);}}
    h1,h2,h3,h4,h5,p,span,div,label {{color: #FFD700 !important; text-shadow: 2px 2px 8px rgba(0,0,0,0.9);}}
    .stMetric {{border-left: 8px solid #FFD700; background: rgba(255,215,0,0.2); border-radius: 14px;}}
    .footer {{text-align:center; padding:5rem; color:#FFD700; font-size:1.5rem;}}
</style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1,4])
with col1:
    st.image(logo, width=300)
with col2:
    st.title("Predaiot")
    st.markdown("### World's First Arabic-Built Profit-Driven Industrial AI")
    st.success("Patent Pending • +15% Revenue Uplift Verified by Muscat Energy (Oman)")

# Leadership
st.markdown("---")
st.subheader("Leadership Team")
col_a, col_b = st.columns(2)
with col_a:
    st.image(chams_photo, caption="Chams Eddine Madi – Founder & CEO", use_column_width=True)
    st.markdown("**Chams Eddine Madi**  \nFounder & CEO • Systems Architect  \n12+ years building profit-optimization AI")
with col_b:
    st.image(sumaiya_photo, caption="Sumaiya – Co-Founder & Strategy", use_column_width=True)
    st.markdown("**Sumaiya**  \nCo-Founder • Strategy & Growth  \nGCC market expert • Investor relations & partnerships")

# PROOF OF VALUE – اللي عايزها تظهر بالظبط
st.markdown("---")
st.image(proof_image, use_column_width=True)

st.markdown(f'''
<div style="text-align:center; margin:80px 0;">
    <a href="{pdf_download}" target="_blank">
        <button style="background:linear-gradient(90deg,#00ff9d,#00d4ff); color:black; font-size:34px; font-weight:bold; padding:30px 140px; border:none; border-radius:30px; box-shadow:0 15px 60px rgba(0,255,157,0.9);">
            Download Official Report (12 Pages)<br>
            <span style="font-size:24px;">+15% Revenue Uplift Verified by Muscat Energy</span>
        </button>
    </a>
</div>
''', unsafe_allow_html=True)

# Financials
st.markdown("---")
st.subheader("5-Year Financial Outlook")
data = {"Year":[2025,2026,2027,2028,2029],"Revenue (£M)":[2.5,6.8,12.5,19.8,28.5],"Cumulative Cash (£M)":[0.7,3.3,8.6,17.6,30.9]}
df = pd.DataFrame(data)

c1,c2,c3,c4 = st.columns(4)
with c1: st.metric("5-Year Revenue", "£70.1M")
with c2: st.metric("Year-5 Cash", "£30.9M")
with c3: st.metric("Year-5 Profit", "£13.3M")
with c4: st.metric("Team 2029", "310")

st.plotly_chart(px.area(df, x="Year", y="Cumulative Cash (£M)", title="Cumulative Cash – Zero to £30.9M",
                        color_discrete_sequence=["#FFD700"], line_shape='spline'), use_container_width=True)

# Footer
st.success("Live Global Dashboard • Patent Pending • Real-World Results Delivered")
st.balloons()

st.markdown("""
<div class="footer">
    © 2025 Predaiot LLC – Registered in Muscat, Sultanate of Oman<br>
    al.shams.invest@gmail.com • +968 7411 4028<br>
    <b>Patent Pending • +15% Revenue Uplift Independently Verified</b>
</div>
""", unsafe_allow_html=True)
