x = input("Enter a series of numbers separated by commas: ")
x = x.split(",")
for i in range(len(x)):
    x[i] = float(x[i])
minx = min(x)
maxx = max(x)
print("Normalized values:")
for i in x:
    print(round((i - minx) / (maxx - minx), 2))