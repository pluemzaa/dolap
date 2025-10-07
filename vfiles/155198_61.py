number_input = list(input("Enter a series of numbers separated by commas: ").split(","))
max = max(number_input)

#loop 0-4
for i in range(5):
	print(f"{number_input[i]} is the maximum value: {max is number_input[i]}")