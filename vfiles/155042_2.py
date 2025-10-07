x = input("Enter a series of numbers separated by commas:")
x = x.split(",")

x[0]= int(x[0])
x[1]= int(x[1])
x[2]= int(x[2])
x[3]= int(x[3])
x[4]= int(x[4])

max=max(x)
min=min(x)

x1=(x[0]-min)/(max-min)
x2=(x[1]-min)/(max-min)
x3=(x[2]-min)/(max-min)
x4=(x[3]-min)/(max-min)
x5=(x[4]-min)/(max-min)

print("%.2f"%x1)
print("%.2f"%x2)
print("%.2f"%x3)
print("%.2f"%x4)
print("%.2f"%x5)