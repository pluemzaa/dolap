input_str = input("Enter numbers separated by commas: ")
numbers = [int(x.strip()) for x in input_str.split(",")]

search_str = input("Enter number to search: ")
try:
    search_num = int(search_str)
except ValueError:
    print(f"No {search_str} found.")
    exit()
found_indices = [i for i, num in enumerate(numbers) if num == search_num]
if found_indices:
    for index in found_indices:
        print(f"Found {search_num} at index {index}")
else:
    print(f"No {search_str} found.")