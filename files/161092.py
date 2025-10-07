input_str = input("Enter a series of numbers separated by commas: ")

numbers = list(map(float, input_str.split(",")))

min_val = min(numbers)
max_val = max(numbers)

normalized = [(x - min_val) / (max_val - min_val) for x in numbers]

print("Normalized values:")
for val in normalized:
    print(f"{val:.2f}")