input_str = input("Enter a series of numbers separated by commas: ")

num_strings = input_str.split(',')
numbers = [int(num.strip()) for num in num_strings]

min_val = min(numbers)
max_val = max(numbers)

print("Normalized values:")

if max_val == min_val:
    for _ in numbers:
        print("0.00")
else:
    for num in numbers:
        normalized_val = (num - min_val) / (max_val - min_val)
        print(f"{normalized_val:.2f}")