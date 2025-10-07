x1 = int(input('Enter the x-coordinate of point 1:'))
y1 = int(input('Enter the x-coordinate of point 1:'))

x2 = int(input('Enter the x-coordinate of point 2:'))
y2 = int(input('Enter the x-coordinate of point 2:'))

slope = ((x2-x1)**2)+((y2-y1)**2)
# print('slope =',slope)
# print('slope^2=',slope**2)
print('the distance between the two points is:'"%.2f"% slope**0.5)