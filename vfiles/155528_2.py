import math
s = input("Enter a series of numbers separated by commas: ")

nums = s.split(",")
nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])
nums[4] = int(nums[4])

print(f"{nums[0]}is the maximus value: {nums[0] is max(nums)}")
print(f"{nums[1]}is the maximus value: {nums[1] is max(nums)}")
print(f"{nums[2]}is the maximus value: {nums[2] is max(nums)}")
print(f"{nums[3]}is the maximus value: {nums[3] is max(nums)}")
print(f"{nums[4]}is the maximus value: {nums[4] is max(nums)}")