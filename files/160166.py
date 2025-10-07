nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])

"""print('max = ',max(nums))
print('min = ',min(nums))"""

Max = nums[0]
for i in range(len(nums)):
    if nums[i] > Max:
        Max = nums[i]
        print("set the maximum value to",nums[i])

print("The maximum value is",Max)