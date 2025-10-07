number = input("Enter a series of numbers separated by commas: ")
numbers = [num(num) for num in number.split(",")]

max_number = max(numbers)
for num in numbers:
	print(f"{num} is the maximum value: {max_number is num}")