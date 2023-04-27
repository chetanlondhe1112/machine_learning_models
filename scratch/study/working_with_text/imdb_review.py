# imdb review 
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
#import streamlit as st
#D:\Private Project\Machine Learning\Project 1\ML_Models\machine_learning_models\scratch\study\data_files\CSV\IMDB-review\train.csv
review=pd.read_csv("scratch/study/data_files/CSV/IMDB-review/train.csv",encoding='iso-8859-1')
print("train file loaded...")

#print(review.dtypes)
text_train=review['text'].to_list()

y_train=review['sentiment'].to_list()

#print(text_train[1])

text_train=[doc.replace("<br />"," ") for doc in text_train]

review_test=pd.read_csv("scratch/study/data_files/CSV/IMDB-review/test.csv",encoding='iso-8859-1')
print("test file loaded....")

#print(review_test.dtypes)
text_test=review_test['text'].to_list()
#print(type(text_test))

y_test=review_test['sentiment'].to_list()

#print(text_train,y_train)
#print(text_test[1])

text_test=[doc.replace("<br />"," ") for doc in text_test]
#print('\n',text_test[1])

vect=CountVectorizer().fit(text_train)
print("vocablury genereted..")
print(len(vect.vocabulary_))

X_train=vect.transform(text_train)
print(X_train.shape)
print("main fetured data genereted....")

features_names=vect.get_feature_names_out()
print(features_names[::2000])