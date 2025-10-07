XF= input("Enter a series of numbers separated by commas: ")
nums = XF.split(",")



nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])
nums[4] = int(nums[4])
XMI = min(nums)
XM = max(nums)

d = (nums[0] - XMI)/(XM-XMI)
e = (nums[1] - XMI)/(XM-XMI)
f = (nums[2] - XMI)/(XM-XMI)
g = (nums[3] - XMI)/(XM-XMI)
h = (nums[4] - XMI)/(XM-XMI)

print("Normalized values:")
print("%.2f"% d)
print("%.2f"% e)
print("%.2f"% f)
print("%.2f"% g)
print("%.2f"% h)

# print(QS1)


# min_x = min(nums)
# max_x = max(nums)
# print(min_x,max_x)
# r0 = nums[0] - min_x
# r1 = nums[1] - min_x
# r2 = nums[2] - min_x
# r3 = nums[3] - min_x