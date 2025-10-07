numbers = input("Enter a series of numbers separated by commas: ")

num_list = [int(n) for n in numbers.split(",")]

maximum = max(num_list)

[print(f"{n} is the maximum value: {(n == maximum) and True or False}") for n in num_list]