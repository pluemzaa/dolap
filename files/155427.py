nums_text = input('Enter a series of numbers separated by commas: ') #==> input
nums = nums_text.split(",")
nums[0] = int (nums[0])
nums[1] = int (nums[1])
nums[2] = int (nums[2])
nums[3] = int (nums[3])
nums[4] = int (nums[4])
x = 10
#result = [90, 0, 10, 4]
_min = min(nums)
_max = max(nums)
x_scaled = (max(nums)-min(nums))

r0 = (nums [0] - _min)/x_scaled
r1 = (nums [1] - _min)/x_scaled
r2 = (nums [2] - _min)/x_scaled
r3 = (nums [3] - _min)/x_scaled
r4 = (nums [4] - _min)/x_scaled

print ('Normalized values:')
print ('%.2f'% r0)
print ('%.2f'% r1)
print ('%.2f'% r2)
print ('%.2f'% r3)
print ('%.2f'% r4)