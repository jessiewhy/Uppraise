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
        #item = str(request.form['item'])
        test = ""
        for key in request.form:
            test=test+", "+key + "= " + request.form[key]
        return "Item: \n" + test
        #data = getListings(item)
       
        """
        X, y = np.array(data[0]).reshape((-1,1)), data[1]
        #define model
        ebay_model= LinearRegression()

        #fit model
        ebay_model.fit(X,y)
        
        pred = [[2]]
        #pred.reshape(1, -1)
        result = str(ebay_model.predict(pred))

        return render_template("balloons.html", result = result)
        """
    else:
        return "else"

@app.route('/', methods = ['GET', 'POST'])
def result():
        return render_template("balloons.html")
    
if __name__ == "__ebayclassifier__":
    app.run(debug=True)