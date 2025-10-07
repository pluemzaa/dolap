nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(',')

for i in range(len(nums)):
    nums[i]=int(nums[i])

max1 = nums[0]
for i in range(len(nums)):
    if nums[i] > max1:
       max1 = nums[i]
       print(f"set the maximum value to {max1}")
    

print(f"The maximum value is {max1}")