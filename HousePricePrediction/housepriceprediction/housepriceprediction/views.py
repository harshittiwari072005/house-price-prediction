from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn import metrics

def home(request):
   
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")

def result(request):
        data = pd.read_csv(r"C:\Users\harsh\OneDrive\Documents\Desktop\houseprice.csv")
        data = data.drop(['Address'],axis=1)
        X = data.drop(['Price'],axis=1)
        y = data['Price']
        X_train,  X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
        model=LinearRegression()
        model.fit(X_train,y_train)
        var1 = float(request.GET['n1'])
        var2 = float(request.GET['n2'])
        var3 = float(request.GET['n3'])
        var4 = float(request.GET['n4'])
        var5 = float(request.GET['n5'])
        pred = model.predict(np.array([var1,var2,var3,var4,var5]).reshape(1,-1))
        pred = round(pred[0])
        price = "The predicted price is $"+str(pred)  
        return render(request, "predict.html",{"result":price})
