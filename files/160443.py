nums = input("Enter numbers separated by commas: ")
numSeach = int(input("Enter number to search: "))
nums = nums.split(",")
found = False


for i in range(len(nums)):
    nums[i] = int(nums[i])
    
for i in range(len(nums)):
    if numSeach == nums[i]:
        print(f"Found {numSeach} at index {i}")
        found = True
        
if not found:
        print(f"No {numSeach} found.")