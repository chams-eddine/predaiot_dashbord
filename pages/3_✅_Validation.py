import streamlit as st
st.image("https://i.imgur.com/SaXlnlg.png", use_column_width=True)
st.success("+15% Revenue Uplift – Independently Verified by Muscat Energy (Oman)")

pdf = "https://drive.google.com/uc?export=download&id=1hL3z1e9v8mK8z9xY7tR5uW2qP9oN6fF_"
st.markdown(f'''
<div style="text-align:center; margin:60px;">
    <a href="{pdf}" target="_blank">
        <button style="background:#00ff9d; color:black; font-size:30px; padding:20px 100px; border:none; border-radius:20px;">
            Download Full 12-Page Report
        </button>
    </a>
</div>
''', unsafe_allow_html=True)
