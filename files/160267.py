num_input = input("Enter numbers separated by commas: ")
num_parts = num_input.split(",")

numbers = []
for part in num_parts:
    part = part.strip()
    if part.lstrip('-').isdigit():
        numbers.append(int(part))

search_input = input("Enter number to search: ")
if search_input.lstrip('-').isdigit():
    search = int(search_input)
else:
    print(f"No {search_input} found.")
    exit()

found = False
for i in range(len(numbers)):
    if numbers[i] == search:
        print(f"Found {search} at index {i}")
        found = True

if not found:
    print(f"No {search} found.")