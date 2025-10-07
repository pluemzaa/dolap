x_1 = int(input("Enter the x-coordinate of point 1:"))
y_1 = int(input("Enter the y-coordinate of point 1:"))
x_2 = int(input("Enter the x-coordinate of point 2:"))
y_2 = int(input("Enter the y-coordinate of point 2:"))
a =  (x_2 - x_1)**2
b = (y_2 - y_1)**2

d = (a+b)**0.5
print(f"The distance between the two points is: {d:.2f}")