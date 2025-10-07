numbers = input("Enter a series of numbers separated by commas: ")

nums = [int(n) for n in numbers.split(",")]

maximum = max(nums)

[print(f"{n} is the maximum value: {(n == maximum) and True or False}") for n in nums]