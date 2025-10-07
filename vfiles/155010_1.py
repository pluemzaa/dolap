nums_text = input('Enter a series of numbers separated by commas:')
nums = nums_text.split(",")
nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])
nums[4] = int(nums[4])

nums = [10,1,5,1,7]
x_max = max(nums)

print(nums[0], 'is the maximum value:',nums[0] is max(nums))
print(nums[1], 'is the maximum value:',nums[1] is max(nums))
print(nums[2], 'is the maximum value:',nums[2] is max(nums))
print(nums[3], 'is the maximum value:',nums[3] is max(nums))
print(nums[4], 'is the maximum value:',nums[4] is max(nums))