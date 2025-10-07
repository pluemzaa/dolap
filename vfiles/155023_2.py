nums = input('Enter a series of numbers separated by commas: ')
nums_ = nums.split(",")

nums_[0] = int(nums_[0])
nums_[1] = int(nums_[1])
nums_[2] = int(nums_[2])
nums_[3] = int(nums_[3])
nums_[4] = int(nums_[4])
x_max = max(nums_)

check_0 = nums_[0] is x_max
check_1 = nums_[1] is x_max
check_2 = nums_[2] is x_max
check_3 = nums_[3] is x_max
check_4 = nums_[4] is x_max

print(f'{nums[0]}is the maximum value: ',check_0 )
print(f'{nums[1]}is the maximum value: ',check_1 )
print(f'{nums[2]}is the maximum value: ',check_2 )
print(f'{nums[3]}is the maximum value: ',check_3 )
print(f'{nums[4]}is the maximum value: ',check_4 )