x1 = int(input('Enter the x-coordinate of point 1:'))
y1 = int(input('Enter the y-coordinate of point 1:'))

x2 = int(input('Enter the x-coordinate of point 2:'))
y2 = int(input('Enter the y-coordinate of point 2:'))

xr = (x2-x1)
yr = (y2-y1)

xrr = xr**2
yrr = yr**2

xyr = xrr + yrr
d  = xyr**0.5
print('The distance between the two points is:%.2f' % d)