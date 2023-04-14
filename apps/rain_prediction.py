# Required modules
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
import streamlit as st
from streamlit_lottie import st_lottie
import json




def lottie_files(file_path=str):
    with open(file=file_path,mode="r") as f:
        return json.load(f)




def rain_model():
    # reading CSV files
    df=pd.read_csv("apps/data_files/CSV/wheather_record.csv")

    # Encoding the string to numericals
    numericals=LabelEncoder()

    # Droping the target variable and make it as newframe
    inputs=df.drop('Play',axis='columns')
    target=df['Play']

    # Creating the new dataframe
    inputs['Outlook_n']=numericals.fit_transform(inputs['Outlook'])
    inputs['Temp_n']=numericals.fit_transform(inputs['Temp'])
    inputs['Hum_n']=numericals.fit_transform(inputs['Humidity'])
    inputs['Win_n']=numericals.fit_transform(inputs['Windy'])

    #Droping the string values
    inputs_n=inputs.drop(['Outlook','Temp','Humidity','Windy'],axis='columns')

    #Applying Naive bayes
    NB_clf=GaussianNB()
    NB_clf.fit(inputs_n,target)

    NB_clf.score(inputs_n,target)

    NB_clf.predict([[0,0,0,1]])

    return NB_clf

def rain_predict(model,data={}):

    np_data=[]
    for i in data:
        if i=="Outlook":
            for x in data[i]:
                if x=='Rainy':
                    np_data.append(1)
                elif x=='Overcast':
                    np_data.append(0)
                elif x=='Sunny':
                    np_data.append(2)

        elif i=="Temperature":
            for x in data[i]:
                if x=='Hot':
                    np_data.append(1)
                elif x=='Mild':
                    np_data.append(2)
                elif x=='Cool':
                    np_data.append(0)

        elif i=="Humidity":
            for x in data[i]:
                if x=='High':
                    np_data.append(0)
                elif x=='Normal':
                    np_data.append(1)
            
        elif i=="Windy":
            for x in data[i]:
                if x=='Yes':
                    np_data.append(1)
                elif x=='No':
                    np_data.append(0)

    res=model.predict([np_data])           
    return res[0]




def rain_predictor_app():

    # APP
    col=st.columns((2,2))

    # Title
    
    col[0].header("⛈ Rain Predictor")

    # inputs

    Outlook=col[0].selectbox("Outlook",options=['Rainy','Overcast','Sunny'])
    Temperature=col[0].selectbox("Temperature",options=['Hot','Mild','Cool'])
    Humidity=col[0].selectbox("Humidity",options=['High','Normal'])
    Windy=col[0].selectbox("Windy",options=['Yes','No'])
   
    

    def lottie_select(output):
        lottie_rainy=lottie_files(file_path="styling/Lotti/rainy.json")
        lottie_sunny=lottie_files(file_path="styling/Lotti/sunny.json")
        lottie_thinking=lottie_files(file_path="styling/Lotti/thinking.json")

        if output=="yes":
            return st_lottie(animation_data=lottie_rainy,speed=1,reverse=False,loop=True,quality="low",height=600)
        elif output=="no":
            return st_lottie(animation_data=lottie_sunny,speed=1,reverse=False,loop=True,quality="low",height=600)
        else:   
            return st_lottie(animation_data=lottie_thinking,speed=1,reverse=False,loop=True,quality="low",height=0,width=600)

    button_col=st.columns((5,5,5))

    if col[0].button("Predict"):
        data={'Outlook':[Outlook],'Temperature':[Temperature],'Humidity':[Humidity],'Windy':[Windy]}
        model=rain_model()
        output=rain_predict(model=model,data=data)

        #out_col[0].title(output)
        with col[1]:
            lottie_select(output=output)
            
    else:
        with col[1]:
            lottie_select(output='') 


