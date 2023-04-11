import streamlit as st
from streamlit_lottie import st_lottie
import json




def lottie_files(file_path=str):
    with open(file=file_path,mode="r") as f:
        return json.load(f)

def lottie_select():
    lottie_intro=lottie_files(file_path="styling/Lotti/hello.json")
    return st_lottie(animation_data=lottie_intro,speed=1,reverse=False,loop=True,quality="low",height=600)
    

def intro():
    col=st.columns((2,2))
    col[0].header("Welcome,")
    col[0].subheader("to my Machine Learning world!")
    with col[1]:
        lottie_select()

