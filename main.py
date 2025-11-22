# main.py → Home
import streamlit as st

st.set_page_config(page_title="Predaiot", page_icon="https://i.imgur.com/dqTpfEc.png", layout="wide")

# خلفية داكنة + ألوان تركواز فاخرة
st.markdown("""
<style>
    .stApp {background: #0a0e1f; background-image: url("https://i.imgur.com/D85r8sz.png"); background-size: cover; background-attachment: fixed;}
    .block-container {background: rgba(10,20,40,0.94); backdrop-filter: blur(15px); border: 2px solid #00ff9d; border-radius: 24px; padding: 3rem; margin: 2rem 0;}
    h1, h2, h3 {color: #00ff9d !important; font-weight: 800;}
    .stButton>button {background: linear-gradient(90deg,#00ff9d,#00d4ff); color:black; font-size:32px; padding:24px 120px; border:none; border-radius:24px; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

st.image("https://i.imgur.com/kExuEFu.png", use_column_width=True)

pdf = "https://drive.google.com/uc?export=download&id=1hL3z1e9v8mK8z9xY7tR5uW2qP9oN6fF_"
st.markdown(f'''
<div style="text-align:center; margin:80px 0;">
    <a href="{pdf}" target="_blank">{st.button("Download Official Report – +15% Revenue Uplift Verified")}</a>
</div>
''', unsafe_allow_html=True)

st.success("Patent Pending • Registered in Muscat, Oman • Live Global Deployment")
st.balloons()
