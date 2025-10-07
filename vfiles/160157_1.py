input_string = input("Enter numbers separated by commas: ")
numbers_list = [int(num) for num in input_string.split(',')
search_number = int(input("Enter number to search: "))
found = False
for index, number in enumerate(numbers_list):
    if number == search_number:
        print(f"Found {search_number} at index {index}")
        found = True 
if not found:
    print(f"No {search_number} found")