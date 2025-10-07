number_input = list(input("Enter a series of numbers separated by commas:").split(","))
max = max(number_input)
for num in number_input:
	print(f"{num} is the maximum value:{max is num}")