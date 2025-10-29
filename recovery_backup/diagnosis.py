import streamlit as st
from web_functions import load_data

def app(df=None, X=None, y=None):
    st.title('Diagnosis')
    if df is None or X is None or y is None:
        try:
            df, X, y = load_data()
        except Exception as e:
            st.error(f'Could not load data: {e}')
            return

    st.write('Dataset preview:')
    st.dataframe(df.head())
