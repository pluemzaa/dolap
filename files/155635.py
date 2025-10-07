numbers = input("Enter a series of numbers separated by commas: ").split(",")
numbers = [int(num) for num in numbers]
maximum = max(numbers)

for num in numbers:
    print(f"{num} is the maximum value: {num == maximum}")