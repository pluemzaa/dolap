nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])

mx = nums[0]
for i in range(len(nums)):
    if nums[i] > mx:
        mx = nums[i]
        print('set the maximum value to',mx) 
print('The maximum value is',mx)