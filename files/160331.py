nums = input("Enter numbers separated by commas: ")
num = int(input("Enter number to search: "))
nums = nums.split(",")
i = 0
for i in range(len(nums)):
    nums[i] = int(nums[i])
    
for i in range(len(nums)):
    if num== nums[i]:
        print(F"Found {num} at index {i}")
else:
    print(f"No {num} found.")