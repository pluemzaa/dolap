nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
s = input("Enter number to search: ")
i=0
while i < len(nums):
    if s==nums[i]:
        print(f"Found {s} at index {i}")
        print(f"Found {s} at index {i}")
        break 
    else:
        print(f"No {s} found.")
        break
    i+=1