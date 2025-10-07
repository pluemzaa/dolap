numbers_str = input("Enter a series of numbers separated by commas: ")
numbers = []
for num_str_item in numbers_str.split(','):
    numbers.append(int(num_str_item.strip()))

_max_value = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > _max_value:
        _max_value = numbers[i]
        print("set the maximum value to " + str(_max_value))

print("The maximum value is " + str(_max_value))