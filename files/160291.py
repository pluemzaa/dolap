nums = input("Enter numbers separated by commas: ")
_search = int(input("Enter number to search: "))

nums = nums.split(",")
for i in range(0,len(nums)):
    nums[i] = int(nums[i])
found = False
for i in range(0,len(nums)):
    if _search == nums[i]:
        print(f"Found {_search} at index {i}")
        found = True

if not found:
    print(f"No {_search} found.")