nums_text = input("Enter a series of numbers separated by commas:")
nums = nums_text.split(",")
x0 = nums[0]
x1 = nums[1]
x2 = nums[2]
x3 = nums[3]
x4 = nums[4]
nums[0] =int(nums[0])
nums[1] =int(nums[1])
nums[2] =int(nums[2])
nums[3] =int(nums[3])
nums[4] =int(nums[4])
print(x0, "is the maximum value:", nums[0] is max)
print(x1, "is the maximum value:", nums[1] is max)
print(x2, "is the maximum value:", nums[2] is max)
print(x3, "is the maximum value:", nums[3] is max)
print(x4, "is the maximum value:", nums[4] is max)