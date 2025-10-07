i = input("Enter a series of numbers separated by commas: ")
nums = i.split(",")


for t in range (len(nums)):
    nums[t] = int(nums[t])
    

for t in range(len(nums)):
    _max = int(input("set the maximum value to "))
    if nums[t] > _max:
        _max = int(input("set the maximum value to "))
        _max = nums[t]
    else:
        break
print('The maximum value is ',max(nums))