input_str = input("Enter a series of numbers separated by commas: ")
numbers = [float(x.strip()) for x in input_str.split(",")]
min_val = min(numbers)
max_val = max(numbers)
print("Normalized values:")
if max_val == min_val:
    for _ in numbers:
        print("0.00")
else:
    for x in numbers:
        normalized = (x - min_val) / (max_val - min_val)
        print(f"{normalized:.2f}")