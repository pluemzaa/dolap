nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(0,len(nums)):
    nums[i] = int(nums[i])

# in case doesnt use funtion
maxval = nums[0]
for i in range(len(nums)):
    if nums[i] > maxval:
        maxval = nums[i]
        print("set the maximum value to ", maxval)
    continue
print('The maximum value is',maxval)