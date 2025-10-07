nums = input("Enter a series of numbers separated by commas: ")
nums= nums.split(",")


for i in range(len(nums)):
    nums[i] = int(nums[i])


_mex = nums[0]

for i in range(len(nums)):
    if(nums[i]) > _mex:
        _mex = nums[i]
        print(f"set the maximum value to{_mex}")
        
        
print(f"The maximum value is {_mex}")