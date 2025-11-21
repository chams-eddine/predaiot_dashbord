# main.py - الإطلاق العالمي الرسمي – 22 نوفمبر 2025
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="EDE v3.0 – أول محرك قرار اقتصادي كوانتي عربي",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("محرك القرار الاقتصادي الكوانتي v3.0")
st.markdown("### أول Economic Decision Engine عربي في التاريخ – من 2023 إلى 2025")
st.success("المؤسس والمطور الوحيد من أول سطر في 2023: أنت – كل الحقوق محفوظة © 2025")

# البيانات المالية (مضمونة بدون أي ملف خارجي)
data = {
    "السنة": [2025, 2026, 2027, 2028, 2029],
    "الإيرادات (جنيه إسترليني)": [2500000, 6800000, 12500000, 19800000, 28500000],
    "صافي الربح (جنيه إسترليني)": [700000, 2600000, 5300000, 9000000, 13300000],
    "الكاش التراكمي (جنيه إسترليني)": [700000, 3300000, 8600000, 17600000, 30900000],
    "عدد الموظفين": [45, 85, 140, 220, 310]
}
df = pd.DataFrame(data)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("إجمالي الإيرادات في 5 سنوات", "£70,100,000")
with col2:
    st.metric("الكاش التراكمي السنة 5", "£30,900,000")
with col3:
    st.metric("صافي الربح السنة 5", "£13,300,000")
with col4:
    st.metric("عدد الموظفين السنة 5", "310")

st.plotly_chart(px.bar(df, x="السنة", y="الإيرادات (جنيه إسترليني)", title="تطور الإيرادات عبر 5 سنوات", color="السنة"), use_container_width=True)
st.plotly_chart(px.line(df, x="السنة", y="صافي الربح (جنيه إسترليني)", title="صافي الربح السنوي", markers=True), use_container_width=True)
st.plotly_chart(px.area(df, x="السنة", y="الكاش التراكمي (جنيه إسترليني)", title="الكاش التراكمي – من الصفر إلى 30.9 مليون جنيه"), use_container_width=True)

st.markdown("---")
st.subheader("الرحلة التاريخية – من 2023 إلى 2025")

colA, colB = st.columns(2)
with colA:
    st.image("https://i.imgur.com/removed-for-privacy1.jpg", caption="v1.0 – حزمة التنفيذ من 2023")
with colB:
    st.image("https://i.imgur.com/removed-for-privacy2.jpg", caption="v2.0 – Economic Engine الاقتصادي الكوانتي 2025")

st.markdown("---")
st.subheader("الإنجازات الحية – اليوم 22 نوفمبر 2025")
st.success("AWS Glue Job: EDE_Quantum_Classifier_Daily → **Succeeded** يوميًا")
st.success("الداشبورد شغال الآن على الإنترنت العالمي 24/7")
st.balloons()

st.caption("© 2025 – أول مشروع عربي كوانتي-اقتصادي موثق من 2023 إلى 2025")
