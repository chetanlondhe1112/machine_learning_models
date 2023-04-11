# Chetan's Machine Learning Models andd training project.

# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from apps.rain_prediction import rain_predictor_app
from apps.intro import intro
# Page styling

st.set_page_config(
        page_title="😎Chetan's ML's🦾",
        page_icon='📈',
        layout="wide",
        initial_sidebar_state="expanded",
    )

with open('styling/CSS/homestyle.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)


# Title Declaration
st.title("😎Chetan's ML's🦾")



# Option Menu
with st.sidebar:
    page = option_menu(
        menu_title="CML's",
        options=['Home','Models'],
        icons=['house',''],
        menu_icon="cast",
        default_index=1
    )

if page=='Home':
    intro()

if page=='Models':
    with st.sidebar:
        models_page = option_menu(
            menu_title="",
            options=['Rain predict','Deseaise'],
            icons=['',''],
            menu_icon="cast",
            default_index=1
        )

    if models_page=="Rain predict":
        rain_predictor_app()
