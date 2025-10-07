import math
x1 = float(input('Enter the x-coordinate of point 1:'))
y1 = float(input('Enter the y-coordinate of point 1:'))
x2 = float(input('Enter the x-coordinate of point 2:'))
y2 = float(input('Enter the y-coordinate of point 2:'))
a = (x2-x1)**2
b = (y2-y1)**2
sum = math.sqrt(a+b)
print("The distance between the two points is:", sum)