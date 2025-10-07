nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

i = 0

for i in range(len(nums)) :
    nums[i] = int(nums[i])
    
x = int(input("Enter number to search: "))
index = 0

for i in range(len(nums)) :
    if nums[i] = x :
    print("found" , x , "at index" , i)
    
else :
    print("No 10 found.")