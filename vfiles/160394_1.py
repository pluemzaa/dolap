ums = input("Enter numbers separated by commas: ")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])
    
max = nums[0]

for i in range(len(nums)):
    if nums[i] > max :
        max = nums[i]
        print('set the maximum value to ' , max)    
print('The maximum value is '  max)