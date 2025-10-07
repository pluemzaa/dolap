nums_text=input("Enter a series of numbers separated by commas: ")
nums=nums_text.split(",")

nums[0]=int(nums[0])
nums[1]=int(nums[1])
nums[2]=int(nums[2])
nums[3]=int(nums[3])
nums[4]=int(nums[4])

max_x=max(nums)

print(nums[0]," is the maximum value: ",nums[0] is max_x)
print(nums[1]," is the maximum value: ",nums[1] is max_x)
print(nums[2]," is the maximum value: ",nums[2] is max_x)
print(nums[3]," is the maximum value: ",nums[3] is max_x)
print(nums[4]," is the maximum value: ",nums[4] is max_x)