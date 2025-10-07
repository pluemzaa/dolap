nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i]=int(nums[i])
    
_max = nums[0]
for i in range(len(nums)):
    if nums[i] > _max:
        _max = nums[i]
        print("set the maximum value to",_max)
    
print("The maximum value is",_max)