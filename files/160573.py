nums = input('Enter a series of numbers separated by commas:')
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])
       
maxx = nums[0]
for i in range(len(nums)):
    if nums[i] > maxx:
        maxx = nums[i]
        print('set the maximum value to ',maxx)    
print('The maximum value is',(maxx))