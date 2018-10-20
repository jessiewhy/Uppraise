import pandas as pd
from ebayScraper import getListings
from sklearn.tree import DecisionTreeRegressor

listingsData = getListings("calculator watch")

#prediction target: price
y= listingsData[1]
print(y) 

#features

X= listingsData[0]

#check
X.describe()

#define model
ebay_model=DecisionTreeRegressor(random_state=1)

#fit model
ebay_model.fit(X,y)
