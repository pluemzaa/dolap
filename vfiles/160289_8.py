nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(".")

for i in range(0,len(nums)):
    nums[i] = int(nums[i])

y = int(input("Enter number to search: "))
for j in range(0,len(nums)):
    if y == nums[j]:
        print(f"Found {y} at index {j}")
    elif y not in nums:
        print(f"No {y} found.")
        break