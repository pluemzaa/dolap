input_str = input("Enter a series of numbers separated by commas: ")
numbers = list(map(int, input_str.split(',')))
max_value = max(numbers)
for num in numbers:
print(f"{num} is the maximum value: {num == max_value}")