nums = input("Enter numbers separated by commas:")
nums = nums.split(",")
x = int(input("Enter number to search:"))
y = x
for i in range(len(nums)):
    nums[i] = int(nums[i])
    
for i in range(len(nums)):
    if y==nums[i]:
        print(f'Found {x} at index', i)
else:
    print(f"no {x} found. ")