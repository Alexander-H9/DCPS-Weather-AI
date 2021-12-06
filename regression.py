import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# get the data
rot =np.array([1,1,1,2,2,3,5,7,7,9,12,13,13,15,20,21])
vel = np.array([1.05,1.04,1.07, 2.08,2.07, 3.08, 5.11, 7.12,7.09, 9.21, 12.22, 13.31, 13.47, 15.52, 20.44, 21.49]) 
assert len(rot) == len(vel), "rot and vel have different size"

# Split the data into training/testing sets
rot_train = rot[0:len(rot)-1:2]
rot_test = rot[1:len(rot):2] 
print("rot train", rot_train, len(rot_train))
print("rot test", rot_test, len(rot_test))

# Split the targets into training/testing sets
vel_train = vel[0:len(vel)-1:2]
vel_test = vel[1:len(vel):2] 
print("vel train", vel_train, len(vel_train))
print("vel test", vel_test, len(vel_test))

# Create linear regression object
regr = linear_model.LinearRegression()


print(rot_train.reshape(-1,1))

# Train the model using the training sets
regr.fit(rot_train.reshape(-1,1), vel_train)

# Make predictions using the testing set
vel_pred = regr.predict(rot_test.reshape(-1,1))

# The coefficients
print("Coefficients: \n", regr.coef_)
# The mean squared error
print("Mean squared error: %.6f" % mean_squared_error(vel_test, vel_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination (Bestimmtheitsmaß): %.6f" % r2_score(vel_test, vel_pred))

# Plot outputs
plt.scatter(rot_test, vel_test)
plt.plot(rot_test, vel_pred, linewidth=3)

plt.xticks(())
plt.yticks(())

plt.title("Linear Regression")
plt.xlabel("Rotations per Second")
plt.ylabel("Velocity in m/s")

plt.show()