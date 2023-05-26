
def average(values):
    return sum(values) / len(values)

def variance(values, average):
    return sum((x - average) ** 2 for x in values)

def covariance(x, average_x, y, average_y):
    return sum((x[i] - average_x) * (y[i] - average_y) for i in range(len(x)))

def weights(x, y):
    x_average, y_average = average(x), average(y)
    b = covariance(x, x_average, y, y_average) / variance(x, x_average)
    a = y_average - b * x_average
    return a, b

def linearly_regress(train_X, train_y, test_X):
    a, b = weights(train_X, train_y)
    predictions = a + b * test_X
    return predictions

# Input values for independent and dependent variables respectively as well as the prediction.
X = []  
Y = [] 
prediction = 


predictions = linearly_regress(X, Y, prediction)

print("Prediction = ", predictions)
