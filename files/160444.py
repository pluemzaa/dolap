nums = input("Enter numbers separated by commas:")
nums = nums.split(",")
find = input("Enter number to search:")

for i in range(len(nums)):
    if find == nums[i]:
        print("Found",find,"at index",i)
else:
    print("No" ,find," found.")