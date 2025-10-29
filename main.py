import streamlit as st
from web_functions import load_data

from Tabs import diagnosis, home, result,  kc, talk2doc

# Configure the app
st.set_page_config(
    page_title = 'Diabetes Prediction System',
    page_icon = '🥯',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

Tabs = {
    "Home":home,
    "Ask Queries":talk2doc,
    "Diagnosis":diagnosis,
    "Result":result,
    "Knowledge Center":kc
}

st.sidebar.title('Navigation')

page = st.sidebar.radio("Page", list(Tabs.keys()))
# Colorful footer: colored heart + gradient-styled name
st.sidebar.markdown(
        """
        <div style="display:flex;align-items:center;gap:8px;margin-top:12px">
            <span style="font-size:18px;color:#ff2d55">❤️</span>
            <span style="font-weight:600">Made with</span>
            <span style="font-weight:700;background:linear-gradient(90deg,#8a2be2,#00c6ff);-webkit-background-clip:text;color:transparent;">
                Subhajyoti
            </span>
    </div>
    """, unsafe_allow_html=True)

df, X, y = load_data()

if page in ["Diagnosis"]:
    Tabs[page].app(df, X, y)
else:
    Tabs[page].app()
