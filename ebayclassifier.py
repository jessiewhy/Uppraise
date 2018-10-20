import pandas as pd
from ebayScraper import getListings
from sklearn.linear_model import LinearRegression 
from sklearn.datasets import make_regression
import numpy as np
from flask import Flask 
app=Flask(__name__)

def getResults(item):
    data = getListings(item)
    
    X, y = np.array(data[0]).reshape((-1,1)), data[1]
    #define model
    ebay_model= LinearRegression()

    #fit model
    ebay_model.fit(X,y)
    
    pred = [[2]]
    #pred.reshape(1, -1)
    return str(ebay_model.predict(pred))

@app.route('/')
def result():
    return "Result: " + getResults("iphone X")
    
if __name__ == "__ebayclassifier__":
    app.run(debug=True)