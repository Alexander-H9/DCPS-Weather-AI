import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import random
import math

# get the data

sd_noise = 0.5                                                         # noise power (=standard deviation)

# v1 =np.array([2.5, 2.6 ,2.7 ,2.8 ,2.9 ,3.0, 2.4, 2.3, 2.2, 2.1, 2.0, 1.9, 1.8, 2.5, 2.6 ,2.7 ,2.8 ,2.9 ,3.0, 2.5])
# v1 = v1 + np.random.normal(0,sd_noise,v1.shape)                         # generate noisy target values 
v1 = np.arange(-3,7,0.01)
v1 = v1 + np.random.normal(0,sd_noise,v1.shape)

# v2 = np.array([2.5, 2.6 ,2.7 ,2.8 ,2.9 ,3.0, 2.4, 2.3, 2.2, 2.1, 2.0, 1.9, 1.8, 2.5, 2.4, 2.3, 2.2, 2.1, 2.0, 2.5]) 
# v2 = v2 + np.random.normal(0,sd_noise,v2.shape)                         # generate noisy target values 
v2 = np.arange(-3,7,0.01)
v2 = v2 + np.random.normal(0,sd_noise,v2.shape)
vSum = np.add(v1, v2)
print("vSum", vSum)
vDif = vSum - 5
print("vDif: ", vDif)

# vel = np.array([0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, 0, 0 ,0 ,0 ,0, 0, 0])
# vel = vel + np.random.normal(0,sd_noise,vel.shape)                      # generate noisy target values 
vel = np.arange(-10,10,0.02)
vel = vel + np.random.normal(0,sd_noise,vel.shape)
assert len(v1) == len(v2), "rot and vel have different size"
assert len(vel) == len(vSum), "vel and vSum habe different size, len(vel)=" + str(len(vel)) + " and len(vSum)=" +str(len(vSum)) 


def calcAngle(p1, p0=(2.5,2.5)):
    print("p1: ", p1)
    if p1[0] == 2.5: p1 = (2.50000000001, *p1[1:])  # handle null division
    # m = (p1[1]-p0[1])/(p1[0]-p0[0])
    deltaY = p1[1] - p0[1]
    deltaX = p1[0] - p0[0]
    alpha = math.atan2(deltaY, deltaX) * 180 / math.pi
    print(alpha)

    if (alpha > 135 and alpha < 180) or (alpha < -135 and alpha > -180): return "East"
    if alpha < -45 and alpha > -134: return "North"
    if (alpha > 0 and alpha < 44) or (alpha > -44 and alpha < 0): return "West"
    if alpha > 45 and alpha < 134: return "South"
    else: return "Failure!!!"

def randomPoint():
    x = random.uniform(2,3)
    y = random.uniform(2,3)
    p = (x,y)
    return p

    

def splitData():

    # Split the data into training/testing sets
    v1_train = v1[0:len(v1)-1:2]
    v1_test = v1[1:len(v1):2] 
    print("v1 train", v1_train, len(v1_train))
    print("v1 test", v1_test, len(v1_test))

    # Split the targets into training/testing sets
    v2_train = v2[0:len(v2)-1:2]
    v2_test = v2[1:len(v2):2] 
    print("\nv1 train", v2_train, len(v2_train))
    print("v1 test", v2_test, len(v2_test))

    # Split the targets into training/testing sets
    vel_train = vel[0:len(vel)-1:2]
    vel_test = vel[1:len(vel):2] 
    print("\nvel train", vel_train, len(vel_train))
    print("vel test", vel_test, len(vel_test))

    # Split the data into training/testing sets
    vSum_train = vSum[0:len(vSum)-1:2]
    vSum_test = vSum[1:len(vSum):2] 
    print("vSum train", vSum_train, len(vSum_train))
    print("vSum test", vSum_test, len(vSum_test))

    return vel_train, vel_test, vSum_train, vSum_test

vel_train, vel_test, vSum_train, vSum_test = splitData()

# Create linear regression object
regr = linear_model.LinearRegression()

print(vSum_train.reshape(-1,1))

# Train the model using the training sets
regr.fit(vSum_train.reshape(-1,1), vel_train)

# Make predictions using the testing set
vel_pred = regr.predict(vSum_test.reshape(-1,1))

# The coefficients
print("Coefficients: \n", regr.coef_)
# The mean squared error
print("Mean squared error: %.6f" % mean_squared_error(vel_test, vel_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination (Bestimmtheitsmaß): %.6f" % r2_score(vel_test, vel_pred))

# Plot outputs
plt.scatter(vSum_test, vel_test)
plt.plot(vSum_test, vel_pred, linewidth=3, c="red")

plt.xticks(())
plt.yticks(())

plt.title("Linear Regression")
plt.xlabel("Sum of the two voltage values")
plt.ylabel("Velocity in m/s")

plt.show()


# calcAngle test
for x in range(10):
    print("\n")
    p = randomPoint()
    print(calcAngle(p))
