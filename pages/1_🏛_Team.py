import streamlit as st

st.title("Leadership Team")

col1, col2 = st.columns([1,2])
with col1:
    st.image("[img]https://i.imgur.com/Nghaveq.jpeg[/img]", use_column_width=True)
with col2:
    st.markdown("""
    ### Chams Eddine Madi  
    **Founder & CEO – PREDAIOT**
    
    Chams is a deep-tech entrepreneur and visionary systems architect with over a decade of early hands-on experience in intelligent automation, data systems, and applied artificial intelligence.

    His journey began in 2012 when his family ran a solar panel cleaning business. The recurring customer question — “Why is efficiency still dropping after cleaning?” — became his obsession.

    While others saw an operational issue, Chams saw an engineering puzzle.

    From teenage years experimenting with hardware logic and predictive models, to building the **Economic Decision Engine™** — a system that doesn’t just predict, but prescribes the most profitable decision in real time.

    **Philosophy:**  
    *Data without decision is noise. Decision without profitability is waste.*

    Chams is building PREDAIOT to become the global standard for profit-driven industrial intelligence.
    """)

st.divider()

col1, col2 = st.columns([1,2])
with col1:
    st.image("[img]https://i.imgur.com/TKRn5oG.jpeg[/img]", use_column_width=True)
with col2:
    st.markdown("""
    ### Sumaiya  
    **Co-Founder & Chief Strategy Officer – PREDAIOT**
    
    Sumaiya is a strategic business architect with deep experience across GCC markets, known for transforming early-stage technologies into scalable commercial opportunities.

    She has worked inside live industrial ecosystems, engaging directly with energy and infrastructure stakeholders across Oman and the wider GCC.

    At PREDAIOT, she leads:
    - Business strategy
    - Investor positioning
    - Partnerships and expansion
    - Market penetration across GCC and India

    Her strength: turning complex deep-tech into powerful business stories that investors and governments act on.

    **Philosophy:**  
    *The future belongs to companies that don’t react — but decide in advance.*
    """)
