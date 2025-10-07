nums_text = input("Enter a series of numbers separated by commas:")
nums = nums_text.split(",")

nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])
nums[4] = int(nums[4])
# r0 = nums[0]
# r1 = nums[1]
# r2 = nums[2]
# r3 = nums[3]
# r4 = nums[4]

print(nums[0]," is the maximum value:",nums[0] == max(nums[0]))
print(nums[1]," is the maximum value:",nums[1] == max(nums[1]))
print(nums[2]," is the maximum value:",nums[2] == max(nums[2]))
print(nums[3]," is the maximum value:",nums[3] == max(nums[3]))
print(nums[4]," is the maximum value:",nums[4] == max(nums[4]))
# print(x)