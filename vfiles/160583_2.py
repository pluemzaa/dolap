x = input("Enter a series of numbers separated by commas: ")
x = x.split(",")

maximum = x[0]
print(f"set the maximum value to {maximum}")

for num in x[1:]:
    if num > maximum:
        maximum = num
        print(f"set the maximum value to {maximum}")

print(f"The maximum value is {maximum}")