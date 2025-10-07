nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")

i=0
for i in range(len(nums)):
    nums[i] = int(nums[i])
    
y = int(input("Enter number to search: "))    
for i in range(len(nums)):
    if nums[i] == y:
        print('Found', y ,' at index ', i)     
indx = 0
if indx == 0:
    print("No",y,"found.")