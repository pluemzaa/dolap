numbers = input("Enter a series of numbers separated by commas: ").split(',')

numbers = [int(num.strip()) for num in numbers]

maximum = max(numbers)

for num in numbers:
    print(f"{num} is the maximum value: {num == maximum}")

numbers = []

for i in range(5):
    value = int(input(f"Enter a series of numbers separated by commas: {i+1}: "))
    numbers.append(value)

maximum = max(numbers)

print("\nvalue:")
for num in numbers:
    print(f"{num} maximum: {num == maximum}")