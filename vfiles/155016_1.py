x = input("Enter a series of numbers separated by commas:")
xlist + x.split(",")

xlist[0]= int(xlist[0])
xlist[1]= int(xlist[1])
xlist[2]= int(xlist[2])
xlist[3]= int(xlist[3])
xlist[4]= int(xlist[4])

xmin = min(xlist)
xmax = max(xlist)

print("Normalized values:")
print("%.2f"%((xlist[0] - xmin)(xmax - xmin)))
print("%.2f"%((xlist[1] - xmin)(xmax - xmin)))
print("%.2f"%((xlist[2] - xmin)(xmax - xmin)))
print("%.2f"%((xlist[3] - xmin)(xmax - xmin)))
print("%.2f"%((xlist[4] - xmin)(xmax - xmin)))