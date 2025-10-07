nums = input("Enter a series of numbers separated by commas: ").split(",")


for i in range(len(nums)):
    nums[i] = int(nums[i])


max_value = nums[0]


for i in range(1, len(nums)):
    if nums[i] > max_value:
        max_value = nums[i]
        print("set the maximum value to", max_value)


print("The maximum value is", max_value)