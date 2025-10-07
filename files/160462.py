nums = input('Enter a series of numbers separated by commas: ')
nums = nums.split(',')

for i in range(len(nums)): 
    nums[i] = int(nums[i])
  
m = nums[0]
for i in range(len(nums)):
    if nums[i] > m: 
        m = nums[i]
        print('set the maximum value to', m)
print('The maximum value is ', m)