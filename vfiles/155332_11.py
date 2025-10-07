x1 = int(input("Enter the x-coordinate of point 1:"))
y1 = int(input("Enter the y-coordinate of point 1:"))
x2 = int(input("Enter the y-coordinate of point 2:"))
y2 = int(input("Enter the y-coordinate of point 2:"))
d = input("The distance between the two points is:")
d = (x2-x1)+(y2-y1)

print('D : %.2f' % d**0.5)