x = input("Enter a series of numbers separated by commas: ")
y = x.split(",")

for i in range(len(y)):
    y[i] = int(y[i])

print(f"Normalized values: ",end = "\n")

for z in y:
    Max = max(y)
    Min = min(y)
    abcd = (z-Min)/(Max-Min)
    print(f"{abcd:.2f}",sep="\n")
#print(f"Normalized values: {abcd:.2f}")