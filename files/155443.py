nums_text = input('Enter a series of numbers separated by commas: ') #==> input
nums = nums_text.split(",")
nums[0] = int (nums[0])
nums[1] = int (nums[1])
nums[2] = int (nums[2])
nums[3] = int (nums[3])
nums[4] = int (nums[4])

_max = max(nums)

r0 = nums [0]
r1 = nums [1] 
r2 = nums [2] 
r3 = nums [3]
r4 = nums [4]

print (nums [0],' is the maximum value: ',r0 == _max)
print (nums [1],' is the maximum value: ',r1 == _max)
print (nums [2],' is the maximum value: ',r2 == _max)
print (nums [3],' is the maximum value: ',r3 == _max)
print (nums [4],' is the maximum value: ',r4 == _max)