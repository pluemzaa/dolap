numbers = input("Enter a series of numbers separated by commas: ")
num_list = [int(n) for n in numbers.split(",")]
maximum = num_list[0]
print(f"set the maximum value to {maximum}")
for num in num_list[1:]:
    if num > maximum:
        maximum = num
        print(f"set the maximum value to {maximum}")
print(f"The maximum value is {maximum}")