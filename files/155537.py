import math

PointX_1 = int(input("Enter the x-coordinate of point 1: "))
PointY_1 = int(input("Enter the y-coordinate of point 1: "))
PointX_2 = int(input("Enter the x-coordinate of point 2: "))
PointY_2 = int(input("Enter the y-coordinate of point 2: "))

distance = ( PointX_2 - PointX_1)**2 + (PointY_2 - PointY_1)**2
squ_distance = math.sqrt(distance)
print("The distance between the two points is: %.2f" % squ_distance)