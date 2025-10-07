numbers = []

for i in range(5):
    num = int(input(f"Enter a series of numbers separated by commas: {i+1}: "))
    numbers.append(num)

maximum = max(numbers)

for num in numbers:
    print(f"{num} is the maximum value: {num == maximum}")