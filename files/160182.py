x = input("Enter a series of numbers separated by commas:").split(",")
for i in range (len(x)) :
    x[i] = int(x[i])
xmax = max(x)
xmin = min(x)
for i in range (len(x)) :
    x[i] = (x[i]-xmin)/(xmax-xmin)
print ("Normalized values: ")
for j in range(len(x)) : 
    xrescaling = x[j]
    print (f"{xrescaling:.2f}")