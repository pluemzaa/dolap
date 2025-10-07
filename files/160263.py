input_str = input("Enter a series of numbers separated by commas: ")

numbers_str = input_str.split(',')
numbers = [float(num.strip()) for num in numbers_str if num.strip()]

min_val = min(numbers)
max_val = max(numbers)

print("Normalized values:")


if max_val == min_val:
    for _ in numbers:
        print("{:.2f}".format(0.00))
else:
    for x in numbers:
        normalized_val = (x - min_val) / (max_val - min_val)
        print("{:.2f}".format(normalized_val))