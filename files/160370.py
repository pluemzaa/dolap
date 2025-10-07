nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")

for i in range(0,len(nums)):
    nums[i] = int(nums[i])

y = int(input("Enter number to search: "))
for h in range(0,len(nums)):
    if y== nums[h]:
        print(f"Found {y} at index {h}")    
    elif y not in nums:
        print(f"No {y} found.")
        break