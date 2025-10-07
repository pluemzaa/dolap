x = input("Enter a series of numbers separated by commas: ")
numbers = list(map(int, x.split(',')))
maximum = max(numbers)
for num in numbers:
    print(f"{num} is the maximum value: {num == maximum}")