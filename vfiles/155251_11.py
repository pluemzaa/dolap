import math 
x1 = int(input("Enter the x-coordinate of point1:"))
y1= int(input("Enter the y-coordinate of point1:"))
x2 = int(input("Enter the x-coordinate of point2:"))
y2 = int(input("Enter the y-coordinate of point2:"))

ds =(math.sqrt)((x2-x1)**2 + (y2-y1)**2)
print('ds : %.2f' % ds)