# x1 =int(input("enter x1"))
# y1 =int(input("enter y1"))
# x2 =int(input("enter x2"))
# y2 =int(input("enter y2"))

# Slope =  (y-2)/(x2-x1)
# print('Slope : %.2f' % Slope)
# Slope = 2
# print('Slope : %.2f' % Slope**2)
# print('Slope : %.2f' % Slope**0.5)

import math
x1 =int(input("Enter the x-coordinate of point 1: "))
y1 =int(input("Enter the y-coordinate of point 1: "))

x2 =int(input("Enter the x-coordinate of point 2: "))
y2 =int(input("Enter the y-coordinate of point 2: "))

math = (math.sqrt)((x2 - x1)**2 +(y2-y1)**2)
print('The distance between the two points is:' , math)