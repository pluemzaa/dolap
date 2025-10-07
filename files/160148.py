nums = input("Enter numbers separated by commas:").split(",")
y = int(input("Enter number to search:"))
#cast str -> int
i = 0
for i in range(len(nums)):
    nums[i] = int(nums[i])

i = 0
for i in range(len(nums)):
    
    if y in nums:
        if y ==nums[i]:
           print(f"Found {y} at index {i}")
    else:
        print(f'No {y} found.')
        break