nums = input("Enter numbers separated by commas:")
nums1 = int(input("Enter number to search:"))
nums = nums.split(",")

y = 0

for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(len(nums)):
    if nums1==nums[i]:
        print('Found' ,nums1, 'at index',i)
        y = 1 
if y==0:
        print("No" ,nums1, "found.")