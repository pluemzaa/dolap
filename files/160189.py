x = input("Enter a series of numbers separated by commas: ").split(',')
for i in range(len(x)):
    x[i] = int(x[i])
i= 0
mn = min(x)
mx = max(x)
print("Normalized values: ")
for i in range(len(x)):
    sum = (x[i]-mn)/(mx-mn)
    print(f"{sum:.2f}")