x1 = int(input("Enter the x-coordinate of point 1: "))
y1 = int(input("Enter the y-coordinate of point 1: "))
x2 = int(input("Enter the x-coordinate of point 2: "))
y2 = int(input("Enter the y-coordinate of point 2: "))

slope1 = (x2-
          x1)**2
slope2 = (y2-y1)**2
d = (slope1 + slope2)**0.5
print('The distanc between the two points is: %.2f' %d)