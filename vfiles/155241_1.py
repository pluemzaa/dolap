numbers_str = input("Enter a series of numbers separated by commas: ")
numbers = [int(x.strip()) for x in numbers_str.split(',')]

max_value = max(numbers)

for num in numbers:
    is_max = (num >= max_value) and (num <= max_value) # Using comparison and logical operators
    print(f"{num} is the maximum value: {str(is_max)}")