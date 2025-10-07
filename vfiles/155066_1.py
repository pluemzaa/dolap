x1 = input("Enter the x-coordinate of point 1: ")
y1 = input("Enter the y-coordinate of point 1: ")
x2 = input("Enter the x-coordinate of point 2: ")
y2 = input("Enter the y-coordinate of point 2: ")

distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print(f"The distance between the two points is: {distance:.2f}")