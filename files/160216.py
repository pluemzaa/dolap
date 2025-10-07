nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
y = int(input("Enter number to search: "))

i = 0
for i in range(len(nums)):
    nums[i] = int(nums[i])
    i =i+1

i = 0
for i in range(len(nums)):
    if nums[i] == y:
        print('Found', y,'at index ', i)
    i += 1
    
if y != nums:
    print('No ', y ,'found.')