nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
s = int(input("Enter number to search: "))

for i in range(0,len(nums)):
    nums[i] = int(nums[i])

for i in range(0,len(nums)):
    if s == nums[i]:
        print(f"Found {s} at index ", i)
        
print(f"No {s} found.")