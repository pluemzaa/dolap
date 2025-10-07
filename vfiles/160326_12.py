nums = input("Enter numbers separated by commas: ")
nums_ = int(input("Enter number to search: "))
nums = nums.split(",")

i = 0

for i in range(0,len(nums)):
    nums[i] = int(nums[i])
    
for i in range(len(nums)):
    if nums_ == nums[i]:
        print('Found',nums_ ,'at index',i)
    
if nums_ != nums[i]:
    print("No",nums_ ,"found.")