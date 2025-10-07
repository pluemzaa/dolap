x = input("Enter a series of numbers separated by commas:")
xlist = x.split(",")

xlist[0]= int(xlist[0])
xlist[1]= int(xlist[1])
xlist[2]= int(xlist[2])
xlist[3]= int(xlist[3])
xlist[4]= int(xlist[4])

xmax = max(xlist)

print(xlist[0],"is the maximum value:",xlist[0] == xmax)
print(xlist[1],"is the maximum value:",xlist[1] == xmax)
print(xlist[2],"is the maximum value:",xlist[2] == xmax)
print(xlist[3],"is the maximum value:",xlist[3] == xmax)
print(xlist[4],"is the maximum value:",xlist[4] == xmax)