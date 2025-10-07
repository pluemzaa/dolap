user = input("Enter a series of numbers separated by commas: ")

nums = [float(x.strip()) for x in user_input.split(",")]

min_val = min(numbers)
max_val = max(numbers)

if max_val == min_val:
    normalized = [0.0 for _ in numbers]
else:
    normalized = [(x - min_val) / (max_val - min_val) for x in numbers]

print("Normalized values:")
for val in normalized:
    print(f"{val:.2f}")