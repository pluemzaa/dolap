nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])
    
Max = nums[0]
Set = 0
for i in range(len(nums)):
    if nums[i] > Max:
        Set = nums[i]
        Max = nums[i]
        print('set the maximum value to',Set)
        
print('The maximum value is',Max)