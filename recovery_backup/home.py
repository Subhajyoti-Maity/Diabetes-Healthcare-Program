import streamlit as st

def app():
    st.title('Home')
    st.write('Welcome to the Diabetes Prediction System. Use the sidebar to navigate.')
import streamlit as st
import PIL
from pathlib import Path


def app():
    st.title('Integrated Diabetes Health Care Program')
    img_path = Path(__file__).resolve().parent.parent / 'images' / 'diabetic.png'
    st.image(str(img_path))

    
    st.markdown(
    """<p style="font-size:20px;">
            Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.
            There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes.
            This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Random Forest Classifier.
        </p>
    """, unsafe_allow_html=True)
    