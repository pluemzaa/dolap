input_str = input("Enter a series of numbers separated by commas: ")
numbers = [float(x.strip()) for x in input_str.split(",")]
min_val = min(numbers)
max_val = max(numbers)

if min_val == max_val:
    print("Normalized values:")
    for _ in numbers:
        print("0.00")
else:
    print("Normalized values:")
    for x in numbers:
        normalized = (x - min_val) / (max_val - min_val)
        print(f"{normalized:.2f}")