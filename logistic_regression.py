import numpy as np
from sklearn.linear_model import LogisticRegression

# Input values for independent and dependent variables respectively as well as the prediction.
X = [[]] 
Y = []
prediction = [[]]

ml = LogisticRegression()
ml.fit(X, Y)

predictions = ml.predict(prediction)

print("Prediction = ", predictions)
