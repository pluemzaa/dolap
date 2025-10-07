nums = input(”Enter numbers separated by commas: “)
nums = nums.split(”,“)

i = 0

for i in range(len(nums)) :
    nums[i] = int(nums[i])
   
x = int(input(”Enter number to search: “))
indx = 0

for i in range(len(nums)) :
    if nums[i] == x :
       print(’Found‘ , x , ’at index‘ , i)
       indx+=1
   
if indx == 0 :
    print(f”No {x} found.“)