input_str = input("Enter a series of numbers separated by commas: ")

numbers = [int(x.strip()) for x in input_str.split(',')]

maximum = numbers[0]

for i in range(1, len(numbers)):
    current_number = numbers[i]
    
    if current_number > maximum:
        maximum = current_number
        print(f"set the maximum value to {maximum}")

print(f"The maximum value is {maximum}")