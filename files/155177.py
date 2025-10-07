nums_text =input("Enter a series of numbers separated by commas:")
nums=nums_text.split(",")
nums[0]=int(nums[0])
nums[1]=int(nums[1])
nums[2]=int(nums[2])
nums[3]=int(nums[3])
nums[4]=int(nums[4])
min_x = min(nums)
max_x = max(nums)
x1=nums[0]-min_x
x2=nums[1]-min_x
x3=nums[2]-min_x
x4=nums[3]-min_x
x5=nums[4]-min_x
z = max_x-min_x
y1=x1/z
y2=x2/z
y3=x3/z
y4=x4/z
y5=x5/z
print("Normalized values:")
print("%.2f" % y1)
print("%.2f" % y2)
print("%.2f" % y3)
print("%.2f" % y4)
print("%.2f" % y5)