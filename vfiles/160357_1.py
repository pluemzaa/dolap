nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

for 1 in range(0,len(nums)):
    nums[1] = int(nums[1])

avg = sum(nums)/len(nums)

s = 0
for 1 in range(0,len(nums)):
    s = s + (nums[1])

s = s/(len(nums)-1)
sd = s ** 0.5
print('Normalized values:',sd)