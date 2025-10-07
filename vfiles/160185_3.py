input_numbers = input("Enter a series of numbers separated by commas: ")
numbers = input_numbers.split(',')

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

maximum = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]
        print("set the maximum value to", maximum)
print("The maximum value is", maximum)