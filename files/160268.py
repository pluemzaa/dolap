d = input("Enter a series of numbers separated by commas: ")
z = [float(i) for i in d.split(',')]
a = min(z)
b = max(z)
print("Normalized values:")
for u in z:
    print(f"{(u - a) / (b - a):.2f}")