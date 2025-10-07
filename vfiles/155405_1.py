import math
x1 = int(input("Enter the x-coordinate of point 1:"))
y1 = int(input("Enter the x-coordinate of point 2:"))
x2 = int(input("Enter the x-coordinate of point 3:"))
y2 = int(input("Enter the x-coordinate of point 1:"))

root = (x2-x1)**2+(y2-y1**2)
root = math.sqrt(root)
print('root: %.2f'%root)