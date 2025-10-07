number_input = list(input("Enter a series of numbers separated by commas: "))
numbers = [int(num) for num in number_input if num != ',']
maxnumber = max(numbers)
for num in number_input:
	print(f"{num} is the maximum value:{max is num}")