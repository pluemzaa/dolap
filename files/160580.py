nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(0,len(nums)):
    nums[i] = int(nums[i])

_max = nums[0]
_min = nums[0]

for h in range(len(nums)):
    if nums[h] > _max:
        _max = nums[h]
        print(f"set the maximum value to {_max}")

print(f"The maximum value is {_max}")