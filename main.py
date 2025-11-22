# main.py – Predaiot EDE v3.0 – Gold Text Edition (Perfect on Dark Background)
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Predaiot – EDE v3.0",
    page_icon="https://i.imgur.com/MZGE157.jpeg",
    layout="wide"
)

# خلفية + نصوص ذهبي فاخر + ظل أسود
st.markdown("""
<style>
    .stApp {
        background: url("https://i.imgur.com/b1lYZqw.jpeg") no-repeat center center fixed;
        background-size: cover;
    }
    .block-container, .css-1d391kg > div {
        background: rgba(5, 10, 30, 0.88) !important;
        backdrop-filter: blur(10px);
        border-radius: 18px;
        padding: 2rem;
        margin: 1rem 0;
    }
    /* كل النصوص ذهبي فاخر مع ظل أسود */
    h1, h2, h3, h4, h5, h6, p, div, span, label, .stMarkdown {
        color: #FFD700 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.9) !important;
        font-weight: 600 !important;
    }
    .stMetric > div > div:first-child {color: #FFD700 !important;}
    .stMetric > div > div:last-child {color: #FFF !important; font-size: 1.8rem !important;}
    .stMetric {border-left: 6px solid #FFD700 !important; background: rgba(255,215,0,0.15) !important;}
    .stSuccess {background: linear-gradient(90deg, #FFD700, #FFA500); -webkit-background-clip: text; -webkit-text-fill-color: transparent;}
    .footer {text-align: center; padding: 3rem; color: #FFD700; font-size: 1.3rem; text-shadow: 2px 2px 6px black;}
</style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://i.imgur.com/MZGE157.jpeg", width=220)
with col2:
    st.title("Predaiot – EDE v3.0")
    st.markdown("### World's First Arabic-Built Quantum Economic Decision Engine")
    st.success("Patent Pending – Official Filing in Progress")

# Founder Info
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

# Charts (ذهبي + ألوان قوية)
chart_config = {"displayModeBar": False}
st.plotly_chart(px.area(df, x="Year", y="Cumulative Cash (£M)", title="Cumulative Cash – Zero to £30.9M",
                        color_discrete_sequence=["#FFD700"]), use_container_width=True, config=chart_config)
st.plotly_chart(px.bar(df, x="Year", y="Revenue (£M)", title="Revenue Growth Trajectory",
                       color_discrete_sequence=["#FFA500", "#FFD700", "#FF8C00", "#FF6347", "#FF4500"]), 
                       use_container_width=True, config=chart_config)

# Journey
st.markdown("---")
st.subheader("From Bedroom 2023 → Global Company 2025")
colA, colB = st.columns(2)
with colA:
    st.image("https://i.imgur.com/2ujGoG4.png", caption="v1.0 – First Arabic Core 2023")
    st.image("https://i.imgur.com/4P5Q48d.png", caption="Project Structure")
with colB:
    st.image("https://i.imgur.com/dzQsCaZ.png", caption="v2.0 Economic Engine 2025")
    st.image("https://i.imgur.com/BvHPeYs.png", caption="Microservices Architecture")

st.image("https://i.imgur.com/eCyISer.png", use_column_width=True)
st.image("https://i.imgur.com/H52AhVg.png", use_column_width=True)

st.success("AWS Glue Job → Running Daily • Live Dashboard 24/7 • Patent Pending")
st.balloons()

# Proof of Value Section – English + Beautiful Download Button
st.markdown("---")
st.subheader("Independent Validation", anchor=False)

col_img, col_text = st.columns([1, 2])
with col_img:
    st.image("https://i.imgur.com/your_new_15percent_image.png", use_column_width=True)  # الصورة اللي بعتها دلوقتي
with col_text:
    st.markdown("""
    ### PREDAIOT: The AI That Unlocked **15% Revenue** on Solar Assets  
    **Independent Validation by Muscat Energy (Oman)**  
    """)
    st.success("+15% Revenue Uplift – **Verified & Documented**")

# زر التحميل الرسمي (إنجليزي + أخضر فاخر)
pdf_url = "https://drive.google.com/file/d/1lW6YJJaUnLJb3NyJuPW4D_tx6RnVYfTa/view?usp=drive_link"

st.markdown(f'''
<div style="text-align: center; margin: 40px 0;">
    <a href="{pdf_url}" target="_blank">
        <button style="
            background: linear-gradient(90deg, #00ff9d, #00d4ff);
            color: black;
            font-size: 22px;
            font-weight: bold;
            padding: 18px 50px;
            border: none;
            border-radius: 16px;
            cursor: pointer;
            box-shadow: 0 8px 20px rgba(0,255,157,0.4);
            transition: all 0.3s;
        "
        onMouseOver="this.style.transform='scale(1.05)'"
        onMouseOut="this.style.transform='scale(1)'">
            Download Official Report – +15% Revenue Uplift (PDF)
        </button>
    </a>
</div>
''', unsafe_allow_html=True)

# Footer ذهبي
st.markdown("""
<div class="footer">
    © 2025 Predaiot LLC – Muscat, Sultanate of Oman<br>
    Contact: al.shams.invest@gmail.com • +968 7411 4028<br>
    <b>Patent Pending • All rights reserved</b>
</div>
""", unsafe_allow_html=True)
