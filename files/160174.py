nums = input("Enter a series of numbers separated by commas:").split(",")
y = 10
#cast str -> int
i = 0
for i in range(len(nums)):
    nums[i] = int(nums[i])
#print('max = ',max(nums))
#print('min = ',min(nums))
Max = nums[0]
for i in range(len(nums)):
    if nums[i] > Max:
        Max = nums[i]
        print('set the maximum value to', Max)
print(f'The maximum value is {Max}')