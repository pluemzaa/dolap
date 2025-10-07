nums = input("Enter numbers separated by commas: ")
nums = nums.split(',')
search = int(input("Enter number to search: "))

for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(len(nums)):
    if nums[i] == search:
        print(f"Found {search} at index {i}")
    elif nums[i] != search:
        continue
    elif i == len(nums) - 1:
        print(f"No {search} found.")