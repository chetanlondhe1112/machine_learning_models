# Packages
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



def spam_LR():

    # Read dataset
    raw_mail_data=pd.read_csv("apps/data_files/CSV/mail_data.csv")
    # replace the null values with a null string
    mail_data=raw_mail_data.where((pd.notnull(raw_mail_data)),'')

    # label spam mail as 0;Non spam mail(num) mail as 1.
    mail_data.loc[mail_data['Category']=='spam','Category']=0
    mail_data.loc[mail_data['Category']=='ham','Category']=1

    # Seperae the data as text & label. x--> text;y-->label
    x=mail_data['Message']
    y=mail_data['Category']

    # Train test split
    x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.2, random_state=3)


    # transform the text data to feature vectors that can be used as input to the Logistic regression
    feature_extraction = TfidfVectorizer(min_df = 1, stop_words='english', lowercase=True)

    x_train_features = feature_extraction.fit_transform(x_train)
    x_test_features = feature_extraction.transform(x_test)

    # convert Y_train and Y_test values as integers
    y_train = y_train.astype('int')
    y_test = y_test.astype('int')


    # training the support vector machine maodel with training data
    model=LogisticRegression()
    model.fit(x_train_features,y_train)

    # Prediction on training data
    prediction_on_training_data=model.predict(x_train_features)
    accuracy_on_training_data=accuracy_score(y_train,prediction_on_training_data)

    # Predction on test data
    prediction_on_test_data=model.predict(x_test_features)
    accuracy_on_test_data=accuracy_score(y_test,prediction_on_test_data)


    return model,accuracy_on_training_data,accuracy_on_test_data,feature_extraction