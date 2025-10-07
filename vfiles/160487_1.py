nums = input("Enter numbers separated by commas:")
nums = nums.split(",")

sn = int(input("Enter number to search:"))

for i in range(len(nums)):
    nums[i] = int(nums[i])
   
for i in range(len(nums)):
    if sn==nums[i]:
        print('Found', sn, 'at index', i)
    else:
        print('No', sn, 'found.')