nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])

p = nums[1]  
for i in range(len(nums)):
    if nums[i] > p:
        p = nums[1]
        break
print('set the maximum value to',p)
print('set the maximum value to',)
print('set the maximum value to',)
print('The maximum value is',max(nums))