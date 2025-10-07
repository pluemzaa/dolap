nums = input("Enter numbers separated by commas:")
y = int(input("Enter number to search:"))
nums = nums.split(",")
c = 0
i = 0
while i < len(nums):
    nums[i] = int(nums[i])
    if y == nums[i]:
        print("Found",y, "at index :",i)
        c+=1
    i+=1
        
    if c == 0:
        print("No" ,y,"found.")