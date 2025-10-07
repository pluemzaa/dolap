input_data = input("Enter a series of numbers separated by commas: ")
numbers = input_data.split(',')

for i in range(len(numbers)):
    numbers[i] = float(numbers[i])

min_value = min(numbers)
max_value = max(numbers)

print("Normalized values:")

for num in numbers:
    if max_value == min_value:
        normalized = 0.0
    else:
        normalized = (num - min_value) / (max_value - min_value)
    print("{:.2f}".format(normalized))