import math

x1, y1, x2, y2 = map(int, input("Enter x1 y1 x2 y2: ").split())

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("The distance between the two points is: %.2f" % d)