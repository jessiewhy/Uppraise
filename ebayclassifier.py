import pandas as pd
from ebayScraper import getListings
from sklearn.linear_model import LinearRegression 
from sklearn.datasets import make_regression
import numpy as np
from flask import Flask, request, render_template
app=Flask(__name__)

@app.route('/py', methods = ['POST', 'GET'])
def getResults():
    if request.method == 'POST':
        item = str(request.form['item'])
        condition = int(request.form['condition'])
        
        data = getListings(item)
       
        
        X, y = np.array(data[0]).reshape((-1,1)), data[1]
        #define models
        ebay_model= LinearRegression()

        #fit model
        ebay_model.fit(X,y)
        
        pred = [[condition]]

        result = str(ebay_model.predict(pred))

        return render_template("index.html", result = str(result))
        

@app.route('/', methods = ['GET', 'POST'])
def result():
        return render_template("index.html")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)