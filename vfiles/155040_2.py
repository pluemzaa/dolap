nums = input('Enter a series of numbers separated by commas: ')
nums = nums.split(',')
num0 = nums[0]
num1 = nums[1] 
num2 = nums[2] 
num3 = nums[3] 
num4 = nums[4] 
num_max = max(nums)

print(num0 ,'is the maximum value:',num0>=num_max)
print(num1 ,'is the maximum value:',num1>=num_max)
print(num2 ,'is the maximum value:',num2>=num_max)
print(num3 ,'is the maximum value:',num3>=num_max)
print(num4 ,'is the maximum value:',num4>=num_max)