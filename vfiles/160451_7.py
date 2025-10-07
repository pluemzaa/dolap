i = input("Enter a series of numbers separated by commas: ")
nums = i.split(",")
f = len(nums)

for t in range (f):
    nums[t] = int(nums[t])
    
_max = nums[0]
for t in range(f):
    if nums[t] > _max:
        _max = nums[t]
        print("set the maximum value to ",_max)


print('The maximum value is ',max(nums))