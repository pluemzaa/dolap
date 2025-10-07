nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

for i in range(0,len(nums)):
    nums[i] = int(nums[i])

_max = nums[0]
_min = nums[0]
for j in range(0,len(nums)):
    if nums[j] >_max:
        _max = nums[j]
        print(f"set the maximum value to {_max}")

print(f"The maximum value is {_max}")