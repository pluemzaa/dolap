nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(0,len(nums)):
    nums[i] = int(nums[i])

# max
_max = nums[0]
for i in range(len(nums)):
    
    if nums[i] > _max:
        
        _max = nums[i]
        
        print("set the maximum value to ",nums[i])

print("The maximum value is ",_max)