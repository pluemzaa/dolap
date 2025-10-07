numbers = [int(x) for x in input("Enter a series of numbers separated by commas: ").split(",")]
max_value = max(numbers)

for num in numbers:
 print(f"{num} is the maximum value: {max_value is num}")