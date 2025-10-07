import math 
x1 = float(input("Enter the x-coordinate of point 1: "))
x2 = float(input("Enter the x-coordinate of point 2: "))
y1 = float(input('Enter the y-coordinate of point 1: '))
y2 = float(input("Enter the y-coordinate of point 2: "))

something = (y2 - y1) / (x2 - x1)
somekind = math.sqrt(something)
print(f"The distance between the two points is: {something:.2f}")