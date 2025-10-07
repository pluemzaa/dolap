input_str = input("Enter numbers separated by commas: ")
numbers = [int(x.strip()) for x in input_str.split(",")]

search_num = int (input("Enter number to search: "))

found_indexes = [i for i, num in enumerate(numbers) if num == search_num]

if found_indexes:
    for idx in found_indexes:
        print(f"Found {search_num} at index {idx}")
else:
    print(f"No {search_num} found.")