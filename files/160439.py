nums = input("Enter numbers separated by commas:")
nums = nums.split(",")
jib =  int(input("Enter number to search:"))
for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(len(nums)):
    if jib==nums[i]:
        print(f"Found {jib:} at index ",i)

else:
    if jib!=nums[i]:
        print(f"No {jib:} found.")