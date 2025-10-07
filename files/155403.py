num_text = (input("Enter a series of numbers separated by commas: "))
nums = num_text.split(",")
nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])
nums[4] = int(nums[4])


value_min = min(nums)
value_max = max(nums)



r1 = nums[0] - value_min
r2 = nums[1] - value_min
r3 = nums[2] - value_min
r4 = nums[3] - value_min
r5 = nums[4] - value_min



z1 = r1 / (value_max - value_min)
z2 = r2 / (value_max - value_min)
z3 = r3 / (value_max - value_min)
z4 = r4 / (value_max - value_min)
z5 = r5 / (value_max - value_min)

print("Normalized values:")
print("%.2f"% z1)
print("%.2f"% z2)
print("%.2f"% z3)
print("%.2f"% z4)
print("%.2f"% z5)