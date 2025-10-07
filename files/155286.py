import math
x1 = float(input('Enter the x-coordinate of point 1:'))
y1 = float(input('Enter the y-coordinate of point 1:'))

x2 = float(input('Enter the x-coordinate of point 2:'))
y2 = float(input('Enter the y-coordinate of point 2:'))

slope = (x2-x1)**2+(y2-y1)**2
#print(math.sqrt((x2-x1)**2+(y2-y1)**2))
square_root = math.sqrt(slope)
print(f'The distance between the two points is: {square_root:.2f}')