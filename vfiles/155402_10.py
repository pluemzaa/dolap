x_scaled = int(input("Enter a series of numbers separated by commas: "))
nums = nums_text.split(",")
x = x-min(x)%max(x)-min(x)


_min = min(nums)
_max = max(nums)
print(_min,_max)
r0 = nums[0] - _min
r1 = nums[1] - _min
r2 = nums[2] - _min
r3 = nums[3] - _min
print("%.2f" % r0)
print("%.2f" % r1)
print("%.2f" % r2)
print("%.2f" % r3)
print =("Normalized values: ")