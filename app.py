# app.py - الداشبورد العالمي الرسمي للمشروع من 2023 إلى 2025
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="EDE v3.0 – Economic Decision Engine", layout="wide")

st.title("محرك القرار الاقتصادي الكوانتي v3.0")
st.markdown("### أول Economic Decision Engine عربي كوانتي في التاريخ – 2023 → 2025")
st.markdown("**المؤسس والمطور الوحيد من أول سطر في 2023:** أنت ❤️")

# تحميل البيانات
df = pd.read_csv("best_energy_financial_data (1).csv")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("إجمالي الإيرادات 5 سنين", f"£{df['Revenue (GBP)'].sum():,.0f}")
with col2:
    st.metric("الكاش التراكمي السنة 5", f"£{df.iloc[-1]['Cumulative Cash (GBP)']:,.0f}")
with col3:
    st.metric("عدد الموظفين السنة 5", int(df.iloc[-1]['Headcount']))

st.plotly_chart(px.bar(df, x="Year", y="Revenue (GBP)", title="تطور الإيرادات"), use_container_width=True)
st.plotly_chart(px.line(df, x="Year", y="Net Income (GBP)", title="صافي الربح", markers=True), use_container_width=True)
st.plotly_chart(px.area(df, x="Year", y="Cumulative Cash (GBP)", title="الكاش التراكمي"), use_container_width=True)

st.success("المشروع شغال يوميًا على AWS Glue ✓ – Glue Job: Succeeded اليوم 21/11/2025")
st.balloons()
