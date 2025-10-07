nums = (input("Enter numbers separated by commas:"))
nums = nums.split(",")


y = int(input("Enter number to search:"))
for i in range(len(nums)):
    nums[i] = int(nums[i])
for i in range(len(nums)):
    if y==nums[i]:
        print('Found',y, 'at index',i)
       
if y not in nums:
    print('NO',y,'found.')