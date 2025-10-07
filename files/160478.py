input_str = input("Enter numbers separated by commas: ")
numbers = list(map(int, input_str.split(',')))

search = int(input("Enter number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == search:
        print(f"Found {search} at index {i}")
        found = True

if not found:
    print(f"No {search} found.")