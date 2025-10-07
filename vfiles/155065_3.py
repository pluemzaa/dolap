x1 = int(input("Enter the x-coordinate of point 1:"))
x2 = int(input("Enter the y-coordinate of point 1:"))
y1 = int(input("Enter the x-coordinate of point 2:"))
y2 = int(input("Enter the y-coordinate of point 2:"))
a = (x2-x1)**2
b = (y2-y1)**2
d = (a+b)**0.5
print("The distance between the two points is:%.2f" % d)