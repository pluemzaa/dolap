numbers = input("Enter a series of numbers separated by commas: ").split(',')

# Convert strings to integers
numbers = [int(num.strip()) for num in numbers]

# Find the maximum value
maximum = max(numbers)