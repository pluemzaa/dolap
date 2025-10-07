# Input a list of numbers separated by commas
numbers_input = input("Enter numbers separated by commas: ")
numbers = [int(x.strip()) for x in numbers_input.split(",")]

# Input the number to search for
target = int(input("Enter number to search: "))

# Search and display results
found = False
for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Found {target} at index {i}")
        found = True

# If not found
if not found:
    print(f"No {target} found.")