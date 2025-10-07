input_str = input("Enter a series of numbers separated by commas: ")

numbers = [float(x.strip()) for x in input_str.split(',')]

min_val = min(numbers)
max_val = max(numbers)

if min_val == max_val:
    scaled = [0.0 for _ in numbers]  
else:
    scaled = [(x - min_val) / (max_val - min_val) for x in numbers]

print("Normalized values:")
for val in scaled:
    print(f"{val:.2f}")