input_str = input("Enter a series of numbers separated by commas: ")

numbers = [int(num.strip()) for num in input_str.split(",")]

maximum = numbers[0]

for num in numbers[1:]:
    if num > maximum:
        maximum = num
        print(f"set the maximum value to {maximum}")

print(f"The maximum value is {maximum}")