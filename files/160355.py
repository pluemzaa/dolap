nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
y = int(input("Enter number to search: "))

for i in range(0,len(nums)):
    nums[i] = int(nums[i])
    
for i in range(0,len(nums)):
    if y == nums[i]:
        print("Found ",y," at index", i)

else:
    print("No ",y," found.")