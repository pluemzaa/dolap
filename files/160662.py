input_str = input("Enter a series of numbers separated by commas: ")
numbers = [float(x) for x in input_str.split(',')]

min_val = min(numbers)
max_val = max(numbers)

print("Normalized values:")
for num in numbers:
    if max_val == min_val:
        print("0.00")
    else:
        normalized = (num - min_val) / (max_val - min_val)
        print("{:.2f}".format(normalized))