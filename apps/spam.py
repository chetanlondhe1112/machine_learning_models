# Import packages

import streamlit as st
from models.spam_lr import *
import json
from streamlit_lottie import st_lottie
import time
import pandas as pd

#D:\Private Project\Machine Learning\Project 1\ML_Models\machine_learning_models\apps\data_files\CSV\mail_data.csv
def read_file():
    df=pd.read_csv('machine_learning_models/apps/data_files/CSV/mail_data.csv')
    return df['Category'].to_list(),df['Message'].to_list()

def lottie_files(file_path=str):
    with open(file=file_path,mode="r") as f:
        return json.load(f)

def lottie_select(output=None):
    lottie_mail=lottie_files(file_path="styling/Lotti/mail.json")
    lottie_spam=lottie_files(file_path="styling/Lotti/spam-email-update.json")
    lottie_green_tick=lottie_files(file_path="styling/Lotti/green_tick.json")

    if output=="spam":
        return st_lottie(animation_data=lottie_spam,speed=1,reverse=False,loop=True,quality="low",height=300)
    elif output=="ham":
        return st_lottie(animation_data=lottie_green_tick,speed=1,reverse=False,loop=True,quality="low",height=250)
    elif output==None:  
        return st_lottie(animation_data=lottie_mail,speed=1,reverse=False,loop=True,quality="low",height=0,width=350)


def spam_page():

    
    if 'predicted' not in st.session_state:
        st.session_state['predicted']=None

    if 'test_text' not in st.session_state:
        st.session_state['test_text']=''

    st.header("📧 Spam mail detetctor:")
    category,messages=read_file()
    sel_col=st.columns((5,1,5,1))
    sel_test_text=sel_col[0].selectbox("Demo Mails:",options=messages)
    sel_col[1].write("")
    sel_col[1].write("")

    if sel_col[1].button("📌"):
        st.session_state['test_text']=sel_test_text
        st.experimental_rerun()

    col=st.columns((1,1))

    


    input_mail=col[0].text_area("Paste your mail here:",height=250,value=st.session_state['test_text'])
    if col[0].button("Detect"):
        if  len(input_mail)>0:
            if input_mail==None:
                col[1].warning("Please paste your mail!!!!")
                time.sleep(2)
                st.session_state['predicted']=None
                st.experimental_rerun()
            else:
                model,train_acc,test_acc,feature_extraction=spam_LR()
                # Convert text to feature vectors
                input_mail_features=feature_extraction.transform([input_mail])
                # making prediction
                prediction=model.predict(input_mail_features)
                st.session_state['predicted']=prediction[0]
                st.experimental_rerun()
        elif len(input_mail)==0:
            col[1].warning("Please paste your mail!!!!")
            time.sleep(2)
            st.session_state['predicted']=None
            st.experimental_rerun()
        
        else:
            col[1].warning("Please paste your mail!!!!")
            time.sleep(2)
            st.session_state['predicted']=None
            st.experimental_rerun()


    with col[1]:
        if st.session_state['predicted']==1:
            st.success("ham")
            lottie_select(output='ham')
        elif st.session_state['predicted']==0:
            st.error("spam")
            lottie_select(output='spam')
        elif st.session_state['predicted']==None:
            lottie_select(output=None)
    
