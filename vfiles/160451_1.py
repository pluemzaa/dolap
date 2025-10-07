i = input("Enter a series of numbers separated by commas: ")
nums = i.split(",")

for t in range (len(nums)):
    nums[t] = int(nums[t])

_max = int(input("set the maximum value to "))
for t in range(len(nums)):
    if nums[i] > _max:
        _max = nums[i]
        
        

print('The maximum value is ',max(nums))