input_numbers = input("Enter numbers separated by commas: ")
numbers = input_numbers.split(',')

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

search = int(input("Enter number to search: "))


found = False
for i in range(len(numbers)):
    if numbers[i] == search:
        print("Found", search, "at index", i)
        found = True

if not found:
    print("No", search, "found.")