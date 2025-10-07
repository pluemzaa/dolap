x1=int(input('enter x1:'))
y1=int(input('enter y1:'))

x2=int(input('enter x2:'))
y2=int(input('enter y2:'))

print('Enter the x-coordinate of point 1:',x1)
print('Enter the y-coordinate of point 1:',y1)

print('Enter the x-coordinate of point 2:',x2)
print('Enter the y-coordinate of point 2:',y2)
d = ((x2-x1)**2 + (y2-y1)**2)**0.5

print("The distance between the two points is:",d)