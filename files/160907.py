input_str = input("Enter a series of numbers separated by commas: ")
numbers = [float(num) for num in input_str.split(',')]

min_val = min(numbers)
max_val = max(numbers)

normalized = []

for x in numbers:
    if max_val == min_val:
        norm_x = 0
    elif x == min_val:
        norm_x = 0
    elif x == max_val:
        norm_x = 1
    else:
        norm_x = (x - min_val) / (max_val - min_val)
    
    normalized.append(round(norm_x, 2))

print("Normalized values:")
for val in normalized:
    print(val)