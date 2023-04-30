# -*- coding: utf-8 -*-
"""diabetes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jQtw9emLon5Vj3jE60xgx_qUu9Sbh3mS
"""

import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

db=pd.read_csv('diabetes.csv')

db.info()



db.describe()

from sklearn.linear_model import LinearRegression

model=LinearRegression()

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test= train_test_split(db[['Glucose','BloodPressure','Insulin','SkinThickness']],db[['Age']])

from sklearn.linear_model import LogisticRegression

model=LogisticRegression(max_iter=1000)

model.fit(x_train,y_train)

y_pred=model.predict(x_test)

y_pred

from sklearn.metrics import classification_report

print(classification_report(y_test,y_pred))

import matplotlib.pyplot as plt

plt.scatter(y_test,y_pred)

