nums = (input("Enter a series of numbers separated by commas:"))
#nums = "10,20,30,40,50"
nums_text = nums.split(",")
nums[0] = int(nums_text[0])
nums[1] = int(nums_text[1])
nums[2] = int(nums_text[2])
nums[3] = int(nums_text[3])
nums[4] = int(nums_text[4])

x = [10,20,30,40,50]
#result = [90, 0, 10, 40]
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