nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
srh = int(input("Enter number to search: "))

for i in range(0,len(nums)):
    nums[i] = int(nums[i])
    
for i in range(0,len(nums)):
    if srh == nums[i]:
        print("Found", srh ,"at index",i )
    
if srh != nums[i]:
    print("No", srh, "found.")