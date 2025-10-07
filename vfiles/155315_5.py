import math

x1=(input("Enter the x-coordinate of point 1:"))
y1=(input("Enter the y-coordinate of point 1:"))
x2=(input("Enter the x-coordinate of point 2:"))
y2=(input("Enter the y-coordinate of point 2:"))

slope = (x2-x1)**2+(y2-y1)**2

print('The distance between the two points is:%.2f'% slope**0.5)