nums_text = "11, 1, 2, 5, 6"
nums = nums_text.split(",")
nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])
nums[4] = int(nums[4])

x = 11

_min = min(nums)
_max = max(nums)
print(_min,_max)
r0 = nums[0] - _min
r1 = nums[1] - _min
r2 = nums[2] - _min
r3 = nums[3] - _min
r4 = nums[4] - _min
print("%.2f" % r0)
print("%.2f" % r1)
print("%.2f" % r2)
print("%.2f" % r3)
print("%.2f" % r4)