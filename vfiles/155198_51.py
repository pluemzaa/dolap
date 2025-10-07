nums = input("Enter a series of numbers separated by commas: ")
numbers = [int(n) for n in nums.split(",")]
max_number = max(numbers)
results = [(n == max_number) and True or False for n in numbers]
for n, res in zip(numbers, results):
    print(f"{n} is the max_number value: {res}")