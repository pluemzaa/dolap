x1 = int(input("Enter the x-coordinate of point 1:Enter numbers"))
x2 = int(input("Enter the y-coordinate of point 1:Enter numbers"))
y1 = int(input("Enter the x-coordinate of point 2:Enter numbers"))
y2 = int(input("Enter the y-coordinate of point 2:Enter numbers"))
distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print('The distance between the two points is: %.2f' % distance)