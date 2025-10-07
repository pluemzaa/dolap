x1 = int(input("Enter the x-coordinate of point 1:"))
y1 = int(input("Enter the y-coordinate of point 1:"))
x2 = int(input("Enter the x-coordinate of point 2:"))
y2 = int(input("Enter the y-coordinate of point 2:"))

x = x2-x1
y = y2-y1
x_1 = x**2
y_1 = x**2

slope = x_1 + y_1

print("The distance between the two points is: %.2f" % slope**0.5)