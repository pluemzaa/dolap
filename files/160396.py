nums = input("Enter numbers separated by commas: ")
nums = nums.split(',')

i = 0

for i in range(0,len(nums)): 
    nums[i] = int(nums[i])
    
y = int(input("Enter number to search:"))
index = 0 

for i in range(len(nums)): 
    if nums[i] == y :
        print('Found ' , y, ' at index ' ,i)
        index= 1
        
if index == 0 :
        print(f"No {y} found.")