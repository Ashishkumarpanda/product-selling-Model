# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15eCgLDUXewpjUnyhAuluDFzvB5UFxVHW
"""

from google.colab import files
a=files.upload()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn import metrics

data=pd.read_csv("iphone-record.csv")
data['Gender'].replace('Male',1,inplace=True)
data['Gender'].replace('Female',0,inplace=True)

data.isnull().sum()

x=data.iloc[:,[0,1,2]].values
y=data.iloc[:,3].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)

reg=LogisticRegression(random_state=0)
reg.fit(x_train,y_train)

pred_y=reg.predict(x_test)

c_m=confusion_matrix(y_test,pred_y)
print('r_square error=',metrics.r2_score(y_test,pred_y))
print('mean square erro=',metrics.mean_squared_error(y_test,pred_y))
print('mean absolute error=',metrics.mean_absolute_error(y_test,pred_y))

x=int(input("input gender"))
y=int(input("input age"))
z=int(input("input salary"))
if x==0 or x==1:
  final_prediction=scaler.fit_transform([[x,y,z]])
  print(reg.predict(final_prediction))
else:
  print("enter valid gender,1-Male: 0-Female")

