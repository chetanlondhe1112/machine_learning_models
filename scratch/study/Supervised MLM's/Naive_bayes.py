# Learning Naive bayes

#imporitng libraries
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import pandas as pd

load_data=load_iris()
x=load_data.data
y=load_data.target
#print(load_data.target)
df=pd.DataFrame(data=load_data.data)
df2=pd.DataFrame(data=load_data.target)
df3=pd.concat([df,df2],axis=1,ignore_index=True)
#print(df3)

x_train,y_train,x_test,y_test=train_test_split(x,y,random_state=3)
#print(x_train,y_train,x_test,y_test)
print(x_test.size)






