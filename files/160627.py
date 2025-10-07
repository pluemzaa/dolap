input_str = input("Enter a series of numbers separated by commas: ")

numbers = [float(x.strip()) for x in input_str.split(",")]

min_val = min(numbers)
max_val = max(numbers)

if max_val == min_val:
    print("All values are the same. Normalized values:")
    for _ in numbers:
        print("0.00")
else:
    print("Normalized values:")
    for x in numbers:
        x_scaled = (x - min_val) / (max_val - min_val)
        print(f"{x_scaled:.2f}")