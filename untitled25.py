# -*- coding: utf-8 -*-
"""Untitled25.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i2MX0lfOQ6sw4hBcedhz157hSDqg8rzk
"""

from google.colab import files
a=files.upload()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn import metrics

data=pd.read_csv("iphone-record.csv")
data['Gender'].replace("Male",0,inplace=True)
data['Gender'].replace("Female",1,inplace=True)
data.head()

data.isnull().sum()

x=data.iloc[:,[0,1,2]].values
y=data.iloc[:,3].values

x_train,x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)

classifier=SVC(kernel='linear',random_state=0)
classifier.fit(x_train,y_train)

pred_y=classifier.predict(x_test)

c_m=confusion_matrix(y_test,pred_y)

print('r2 score=',metrics.r2_score(y_test,pred_y))

x=int(input("Enter Gender"))
if x==0 or x==1:
  y=int(input("Enter age"))
  z=int(input("Enter Salary"))
  final_prediction=classifier.predict([[x,y,z]])
  print(final_prediction)
else:
  print("Enter valid Gender,0 for Male and 1 For Female")