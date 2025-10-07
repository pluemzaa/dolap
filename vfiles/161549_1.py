import math

x1 = int(input("Enter x1 = "))

y1 = int(input("Enter x2 = "))

x2= int(input("Enter y1 = "))

<>

y2 = int(input("Enter y2 = "))

dif_x_pow2 = math.pow(x1-x2,2)

OT

dif_y_pow2 = math.pow(y1-y2,2)

distance =math.sqrt(dif_x_pow2 + dif_y_pow2)

print("Euclidean distance", distance)

dif_x_m2 = math.fabs(x1-x2)

dif_y_m2 = math.fabs (y1-y2)

distance1 =abs(dif_x_m2 + dif_y_m2)

print("Manhattan distance", distance1)