a = input("Enter a series of numbers separated by commas: ")
b = [float(x) for x in a.split(",")]
min_val = min(b)
max_val = max(b)

if max_val == min_val:
    print("Normalization is not possible because all values are equal.")
else:
    print("Normalized values:")
    for x in b:
        normalized = (x - min_val) / (max_val - min_val)
        print(f"{normalized:.2f}")