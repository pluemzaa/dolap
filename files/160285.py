num = input("Enter a series of numbers separated by commas: ")
numbers = [float(x.strip()) for x in num.split(",")]

Min = min(numbers)
Max = max(numbers)

if Max == Min:
    normalized = [0.0 for _ in numbers]
else:
    normalized = [(x - Min) / (Max - Min) for x in numbers]

print("Normalized values:")
for val in normalized:
    print(f"{val:.2f}")