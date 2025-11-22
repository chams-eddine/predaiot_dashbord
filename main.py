# main.py
import streamlit as st

st.set_page_config(
    page_title="Predaiot – Profit-Driven AI",
    page_icon="https://i.imgur.com/MZGE157.jpeg",
    layout="wide"
)

# خلفية + ألوان تركواز فاخرة
st.markdown("""
<style>
    .stApp {background: #0a0e1f; background-image: url("https://i.imgur.com/b1lYZqw.jpeg"); background-size: cover;}
    .block-container {background: rgba(10,20,40,0.95); backdrop-filter: blur(12px); border: 1px solid #00ff9d; border-radius: 20px; padding: 2rem;}
    h1, h2, h3 {color: #00ff9d !important;}
</style>
""", unsafe_allow_html=True)

st.image("https://i.imgur.com/8vK3k9P.png", use_column_width=True)

pdf = "https://drive.google.com/uc?export=download&id=1hL3z1e9v8mK8z9xY7tR5uW2qP9oN6fF_"
st.markdown(f'''
<div style="text-align:center; margin:70px;">
    <a href="{pdf}" target="_blank">
        <button style="background:#00ff9d; color:black; font-size:32px; padding:22px 120px; border:none; border-radius:20px; font-weight:bold;">
            Download Official Report (+15% Revenue Uplift)
        </button>
    </a>
</div>
''', unsafe_allow_html=True)

st.success("Patent Pending • Registered in Muscat, Oman • Real-World Results Delivered")
