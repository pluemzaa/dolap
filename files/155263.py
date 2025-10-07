x1 = input('Enter the x-coordinate of point 1: ')
y1 = input('Enter the y-coordinate of point 1: ')
x2 = input('Enter the x-coordinate of point 2: ')
y2 = input('Enter the y-coordinate of point 2: ')

x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

import math


d = (x1-x2) **2  + (y1-y2) **2
d = (math.sqrt(d))


print("The distance between the two points is: %.2f" %d)