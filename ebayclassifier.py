import pandas as pd
from ebayScraper import getListings
from sklearn.linear_model import LinearRegression 
from sklearn.datasets import make_regression
import numpy as np

data = getListings("iphone X")


X, y = np.array(data[0]).reshape((-1,1)), data[1]
#define model
ebay_model= LinearRegression()



#fit model
ebay_model.fit(X,y)

pred = [[2]]
#pred.reshape(1, -1)
print(ebay_model.predict(pred))
