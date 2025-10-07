nums = input("Enter numbers separated by commas: ")
nums_ = int(input("Enter number to search: "))
nums = nums.split(",")

y = nums_

for i in range(0,len(nums)):
    nums[i] = int(nums[i])
    
if y != nums[i]:
    print("No",y ,"found.")
   
    
for i in range(0,len(nums)):
    if y == nums[i]:
        print("Found",y ,"at index",i)