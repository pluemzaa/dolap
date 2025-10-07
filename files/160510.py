nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])
Maxga = nums[0]
for i in range(len(nums)):
    if nums[i] > Maxga:
        Maxga = nums[i]
        
        
        print('set the maximum value to', Maxga)
print('The maximum value is ', Maxga)