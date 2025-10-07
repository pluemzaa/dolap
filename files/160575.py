nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])
    
p = nums[0]
for i in range(len(nums)):
    if nums[i] > p:
        p = nums[i]
        print('set the maximum value to',p)
        
print('The maximum value is',p)