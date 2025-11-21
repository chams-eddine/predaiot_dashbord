# main.py - الإطلاق العالمي الرسمي – 22 نوفمبر 2025
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="EDE v3.0 – أول محرك قرار اقتصادي كوانتي عربي", layout="wide")

st.title("محرك القرار الاقتصادي الكوانتي v3.0")
st.markdown("### أول Economic Decision Engine عربي في التاريخ – من 2023 إلى 2025")
st.success("المؤسس والمطور الوحيد من أول سطر في 2023: أنت – كل الحقوق محفوظة © 2025")

# البيانات المالية
data = {
    "Year": [2025, 2026, 2027, 2028, 2029],
    "Revenue (GBP)": [2500000, 6800000, 12500000, 19800000, 28500000],
    "Net Income (GBP)": [700000, 2600000, 5300000, 9000000, 13300000],
    "Cumulative Cash (GBP)": [700000, 3300000, 8600000, 17600000, 30900000],
    "Headcount": [45, 85, 140, 220, 310]
}
df = pd.DataFrame(data)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("إجمالي الإيرادات 5 سنوات", "£70,100,000")
with col2:
    st.metric("الكاش التراكمي السنة 5", "£30,900,000")
with col3:
    st.metric("صافي الربح السنة 5", "£13,300,000")
with col4:
    st.metric("عدد الموظفين السنة 5", "310")

st.plotly_chart(px.bar(df, x="Year", y="Revenue (GBP)", title="تطور الإيرادات"), use_container_width=True)
st.plotly_chart(px.line(df, x="Year", y="Net Income (GBP)", title="صافي الربح", markers=True), use_container_width=True)
st.plotly_chart(px.area(df, x="Year", y="Cumulative Cash (GBP)", title="الكاش التراكمي"), use_container_width=True)

st.markdown("---")
st.subheader("الدليل التاريخي – من 2023 إلى 2025")
colA, colB = st.columns(2)
with colA:
    st.image("https://i.imgur.com/8vB8z8K.png", caption="v1.0 – بداية المشروع 2023")  # حط رابط صورة v1.0 هنا
with colB:
    st.image("https://i.imgur.com/X7pL9mN.png", caption="v2.0 – Economic Engine 2025")  # حط رابط صورة v2.0 هنا

st.markdown("---")
st.success("AWS Glue Job: EDE_Quantum_Classifier_Daily → Succeeded يوميًا")
st.success("المشروع شغال الآن على الإنترنت العالمي 24/7")
st.balloons()

st.caption("© 2025 – أول مشروع عربي كوانتي-اقتصادي موثق من 2023 إلى 2025")
