#12,4,10,40,30,10
nums = input("Enter")
nums = nums.split(",")

for 1 in range(0,len(nums)):
    nums[1] = int(nums[1])
 
_max = nums[0]
for 1 in range(len(nums)):
    if nums[1] > _max:
        _max = nums[1]

print("max = ",_max)

print("max", max(nums))
print("min", min(nums))
print('sum', sum(nums))