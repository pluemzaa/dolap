nums_str = input("Enter a series of numbers separated by commas: ")
nums = [float(x.strip()) for x in nums_str.split(",")]

x_min = min(nums)
x_max = max(nums)

print("Normalized values:")

r0 =(nums[0]-x_min)/(x_max-x_min)
r1 =(nums[1]-x_min)/(x_max-x_min)
r2 =(nums[2]-x_min)/(x_max-x_min)
r3 =(nums[3]-x_min)/(x_max-x_min)
r4 =(nums[4]-x_min)/(x_max-x_min)

print("%.2f" % r0)
print("%.2f" % r1)
print("%.2f" % r2)
print("%.2f" % r3)
print("%.2f" % r4)