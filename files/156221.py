numbers = list(map(int, input("Enter a series of numbers separated by commas: ").split(",")))
maximum = max(numbers)
for num in numbers:
    print(f"{num} is the maximum value: {num == maximum}")