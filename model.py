# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.

import math
import random
#find x0 and y0
print("find y0 and x0")
# Set up variables.
y0 = 0
x0 = 0
print ("y0: ", y0)
print ("x0: ",x0)
# Random walk one step find the y.
random_numberY = random.random()
print ("random number: ",random_numberY)
if random_numberY < 0.5:
    y0 += 1
else:
    y0 -= 1
print ("if random number < 0.5")
print ("y0= y0+1")
print ("else")
print("y0= y0-1")
print("y0: ",y0)
# Random walk one step find the x.
random_numberX = random.random()
print ("random number: ",random_numberX)
if random_numberX < 0.5:
    x0 += 1
else:
    x0 -= 1
print ("if random number < 0.5")
print ("x0= x0+1")
print ("else")
print("x0= x0-1")
print("x0: ",x0)
print("y0: ",y0)

#find x1 and y1
print("")
print("find y1 and x1")
# Set up variables.
y1 = 4
x1 = 3
print ("y1: ", y1)
print ("x1: ",x1)
# Random walk one step find the y.
random_numberY = random.random()
print ("random number: ",random_numberY)
if random_numberY < 0.5:
    y1 += 1
else:
    y1 -= 1
print ("if random number < 0.5")
print ("y1= y1+1")
print ("else")
print("y1= y1-1")
print("y1: ",y0)
# Random walk one step find the x.
random_numberX = random.random()
print ("random number: ",random_numberX)
if random_numberX < 0.5:
    x1 += 1
else:
    x1 -= 1
print ("if random number < 0.5")
print ("x1= x1+1")
print ("else")
print("x1= x1-1")
print("x1: ",x0)

#find distance between two coordinates
print("")
print("distance between two coordinates")

y0 = 0
x0 = 0
y1 = 4
x1 = 3


y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum**0.5
print("distance: ",answer)

print ( math.sqrt (16))
print ( 16**0.5)