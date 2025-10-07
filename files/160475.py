input_str = input("Enter a series of numbers separated by commas: ")
numbers = [float(x.strip()) for x in input_str.split(",")]

min_val = min(numbers)
max_val = max(numbers)

if max_val == min_val:
    normalized = [0.0 for _ in numbers]
else:
    normalized = [(x - min_val) / (max_val - min_val) for x in numbers]

print("Normalized values:")
for value in normalized:
    print(f"{value:.2f}")