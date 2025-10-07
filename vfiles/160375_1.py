nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(0,len(nums)):
    nums[i] = int(nums[i])

# in case doesnt use funtion
_max = nums[0]
for i in range(len(nums)):
    if nums[i] > _max:
        _max = nums[i]
        print("set the maximum value to ", i)
    continue
print('The maximum value is',_max)