nums = input("Enter numbers separated by commas: ")
nums_ = int(input("Enter number to search: "))
nums = nums.split(",")

i = 0

for i in range(0,len(nums)):
    nums[i] = int(nums[i])
    
if nums_ != nums[i]:
    print("No",nums_ ,"found.")
   
    
for i in range(0,len(nums)):
    if nums_ == nums[i]:
        print("Found",nums_ ,"at index",i)