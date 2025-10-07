n1 = (input('Enter a series of numbers separated by commas:'))

x =  [float(i.strip()) for i in n1.split(',')]

min = min(x)
max = max(x)

print("Normalized values:")

if max == min:
    for _ in x:
        print("0.00")
else:
    for xi in x:
        normalized = (xi - min) / (max - min)
        print(f"{normalized:.2f}")