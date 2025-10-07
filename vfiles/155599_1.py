numbers = input("Enter a series of numbers separated by commas: ").split(',')
numbers = [int(num) for num in numbers]

maximum = max(numbers)

results = [str(num) + " is the maximum value: " + str(num == maximum) for num in numbers]

print('\n'.join(results))