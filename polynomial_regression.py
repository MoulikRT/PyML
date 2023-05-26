import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Input values for independent and dependent variables respectively as well as the prediction and degree.
X = []  
Y = []  
degree = 2
prediction = [] 

polynomial = PolynomialFeatures(degree)
X_value = polynomial.fit_transform(X)

ml = LinearRegression()
ml.fit(X_value, Y)

prediction_value = poly_transform.transform(prediction)
predictions = ml.predict(prediction_value)

print("Prediction = ", predictions)
