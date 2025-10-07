input_str = input("Enter a series of numbers separated by commas: ")
numbers = [int(x.strip()) for x in input_str.split(',')]

maximum = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]
        print(f"set the maximum value to {maximum}")

print(f"The maximum value is {maximum}")