nums = input ("Enter numbers separated by commas:")
nums = nums.split(",")
for i in range(0,len(nums)):
    nums[i] = int(nums[i])
search = int(input("Enter number to search:"))
for j in range(0,len(nums)):
    if search== nums[j]:
        print(f"Found {search} at index {j}")
if search not in nums:
    print(f"No {search} found.")