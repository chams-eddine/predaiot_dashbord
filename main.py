# main.py → Home + Full Dashboard (النسخة الملكية اللي عايزها بالظبط)
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Predaiot – +15% Revenue AI", page_icon="https://i.imgur.com/dqTpfEc.png", layout="wide")

# خلفية + ألوان تركواز فاخرة
st.markdown("""
<style>
    .stApp {background: #0a0e17; background-image: url("https://i.imgur.com/D85r8sz.png"); background-size: cover; background-attachment: fixed;}
    .block-container {background: rgba(5,15,35,0.94); backdrop-filter: blur(16px); border: 2px solid #00ff9d; border-radius: 28px; padding: 3rem; margin: 2rem 0;}
    h1, h2, h3, h4 {color: #00ff9d !important; font-weight: 800;}
    .stMetric {background: rgba(0,255,157,0.15); border-left: 6px solid #00ff9d; border-radius: 16px; padding: 1rem;}
    .stButton>button {background: linear-gradient(90deg,#00ff9d,#00d4ff); color:black; font-size:34px; padding:28px 140px; border:none; border-radius:28px; font-weight:bold; box-shadow: 0 10px 40px rgba(0,255,157,0.6);}
</style>
""", unsafe_allow_html=True)

# الصورة الرئيسية الجديدة (التحفة)
st.image("https://i.imgur.com/kExuEFu.png", use_column_width=True)

# الأرقام المليونية
st.markdown("### 5-Year Financial Outlook")
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("5-Year Revenue", "£70.1M", delta="+2800% growth")
with col2: st.metric("Year-5 Cash", "£30.9M", delta="Self-funded")
with col3: st.metric("Year-5 Profit", "£13.3M", delta="47% margin")
with col4: st.metric("Team 2029", "310", delta="Global scale")

# الجراف الذهبي
data = {"Year":[2025,2026,2027,2028,2029],"Cumulative Cash (£M)":[0.7,3.3,8.6,17.6,30.9]}
df = pd.DataFrame(data)
fig = px.area(df, x="Year", y="Cumulative Cash (£M)", 
              title="Cumulative Cash – Zero to £30.9M in 5 Years",
              color_discrete_sequence=["#00ff9d"], line_shape='spline')
fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font_color="#00ff9d")
st.plotly_chart(fig, use_container_width=True)

# زر تحميل التقرير الرسمي
pdf = "https://drive.google.com/uc?export=download&id=1hL3z1e9v8mK8z9xY7tR5uW2qP9oN6fF_"
st.markdown(f'''
<div style="text-align:center; margin:90px 0;">
    <a href="{pdf}" target="_blank">
        <button>Download Official 12-Page Report<br><span style="font-size:24px;">+15% Revenue Uplift Verified by Muscat Energy</span></button>
    </a>
</div>
''', unsafe_allow_html=True)

# الحالة الحية
st.success("AWS Glue Job Running Daily • Live Global Dashboard • Patent Pending")
st.balloons()

# الفوتر
st.markdown("""
<div style="text-align:center; padding:4rem; color:#00ff9d; font-size:1.4rem;">
    © 2025 Predaiot LLC – Registered in Muscat, Sultanate of Oman<br>
    al.shams.invest@gmail.com • +968 7411 4028<br>
    <b>Patent Pending • +15% Revenue Uplift Independently Verified</b>
</div>
""", unsafe_allow_html=True)
