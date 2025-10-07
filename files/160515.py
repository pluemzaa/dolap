nums = input("Enter a series of numbers separated by commas: ").split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])

_max = nums[0]
for i in range(len(nums)):
    if nums[i] > _max:
        _max = nums[i]
        print(F"set the maximum value to {_max}")
print(F"The maximum value is {_max}")