x1 = int(input("Enter the x-coordinate of point 1: "))
y1 = int(input("Enter the y-coordinate of point 1: "))

x2 = int(input("Enter the x-coordinate of point 2: "))
y2 = int(input("Enter the y-coordinate of point 2: "))

slope = (y2-y1)**2+(x2-x1)**2
n = slope**0.5
print(f"The distance between the two points is : {n:.2f}")