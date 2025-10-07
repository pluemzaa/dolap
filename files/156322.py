numbers = input("Enter a series of numbers separated by commas: ")
num_list = list(map(int, numbers.split(",")))
max_value = max(num_list)
results = [print(f"{n} is the maximum value: {(n == max_value) and True or False}") for n in num_list]