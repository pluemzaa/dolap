numbers = list(map(int, input("Enter a series of numbers separated by commas: ").split(',')))
maximum = max(numbers)
results = [(str(n) + " is the maximum value: " + str(n == maximum)) for n in numbers]
print('\n'.join(results))