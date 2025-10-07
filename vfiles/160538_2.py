def main():
    nums_input = input("Enter numbers separated by commas: ")
    
    nums = [int(x.strip()) for x in nums_input.split(',')]
    target = int(input("Enter number to search: "))

    found = False
    for index, value in enumerate(nums):
        if value == target:
            print(f"Found {target} at index {index}")
            found = True

    if not found:
        print(f"No {target} found.")

if __name__ == "__main__":
    main()