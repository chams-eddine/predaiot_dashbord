import streamlit as st
st.title("Leadership Team")

col1, col2 = st.columns(2)
with col1:
    st.image("https://i.imgur.com/BUuOchX.jpeg", use_column_width=True)
    st.markdown("**Chams Eddine Madi**  \nFounder & CEO  \n12+ years building profit-driven AI systems  \nStarted in solar asset optimization → created the Economic Decision Engine™")
with col2:
    st.image("https://i.imgur.com/VtGeq0W.jpeg", use_column_width=True)
    st.markdown("**Sumaiya**  \nCo-Founder & Chief Strategy Officer  \nGCC market expert • Investor relations • Regional scaling across MENA & India")
