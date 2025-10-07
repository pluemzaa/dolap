nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
numx = int(input("Enter number to search: "))
i = 0
for i in range(0,len(nums)):
    nums[i] = int(nums[i])
for i in range(0,len(nums)):
    if numx == nums[i]:
        print(f"Found {numx} at index", i)
    
else:
    print(f"No {numx} found.")