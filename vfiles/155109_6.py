x1 = int(input("Enter the x-coordinate of point 1:"))
y1 = int(input("Enter the y-coordinate of point 1:"))

x2 = int(input("Enter the x-coordinate of point 2:"))
y2 = int(input("Enter the y-coordinate of point 2:"))

xruam = (x2-x1)
ywhat = (y2-y1)

yok = xruam**2
kamlang = ywhat**2

ruam = yok + kamlang
print('The distance between the two points is: %.2f' %ruam)