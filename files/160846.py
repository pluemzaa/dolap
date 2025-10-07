nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(',')

for i in range(len(nums)):
    nums[i] = int(nums[i])
maximum = nums[0]
for num in range(len(nums)):
    if nums[num] > maximum:
        maximum = nums[num]
        maximum = nums[num]
        print("set the maximum value to", maximum)
print("The maximum value is", maximum)