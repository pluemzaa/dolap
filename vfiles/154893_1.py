import math
x1 = float(input('Enter the x-coordinate of point 1:'))
y1 = float(input('Enter the y-coordinate of point 1:'))
x2 = float(input('Enter the x-coordinate of point 2:'))
y2 = float(input('Enter the y-coordinate of point 2:'))
a = (x2-x1)
b = (y2-y1)
sum = math.sqrt(a)**2 + (b)**2
print("The distance between the two points is:", sum)