import numpy as np
from sklearn.linear_model import LinearRegression

# Input values for independent and dependent variables respectively as well as the prediction.
X = [[]]
Y = [] 
prediction =[[]]

ml = LinearRegression()
ml.fit(X, Y)

predictions = ml.predict()

print("Prediction = ", predictions)
