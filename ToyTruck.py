""""This example predicst the time it takes a toy truck to travel a distance"""

import numpy as np
from sklearn import linear_model

# Initialise arrays
inputArray = []
outputArray = []

# Inputs are [DISTANCE, POWER]
# Distance is in m
# Car has a NORMAL = 1 and POWER = 2 modes of operation

# NORMAL MODE DATA
# ================


# Entry 1
inputArray.append([1.0, 1])
outputArray.append(6.5)

# Entry 2
inputArray.append([2.0, 1])
outputArray.append(12.38)

# Entry 3
# This is our test data, hence commented out
# inputArray.append([3.0, 1])
# outputArray.append(18.68)

# Entry 4
inputArray.append([4.0, 1])
outputArray.append(24.57)

# Entry 5
inputArray.append([5.0, 1])
outputArray.append(30.0)


# POWER MODE DATA
# ===============

# Entry 6
inputArray.append([1.0, 2])
outputArray.append(4.0)

# Entry 7
inputArray.append([2.0, 2])
outputArray.append(6.5)

# Entry 8
# This is our test data, hence commented out
# inputArray.append([3.0, 2])
# outputArray.append(9.53)

# Entry 9
inputArray.append([4.0, 2])
outputArray.append(12.65)

# Entry 10
inputArray.append([5.0, 2])
outputArray.append(15.65)

# Turn lists into NumPy arrays
inputData = np.array(inputArray)
outputData = np.array(outputArray)

# Turn data into a model
reg = linear_model.LinearRegression()
reg.fit (inputData, outputData)
reg.coef_

print ("Predicted time to travel 3m is ", reg.predict([[3.0, 1]]))
