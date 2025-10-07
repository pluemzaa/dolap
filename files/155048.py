x = input("Enter a series of numbers separated bt commas: ").spilt(";")
for i in range(len(x)):
   x[i] = int(x[i])

x_max,x_min = max(x),min(x)
x_scaled = []
print("Normalized values: ")
for i in range(len(x)):
 x_scaled += [((x[i] - min(x)))/max(x-min(x))]
 print("%.2f"%x_scaled[i])