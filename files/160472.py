nums = input("Enter numbers separated by commas:")
nums = nums.split(",")
s = int(input("Enter number to search:"))
y = 0

for i in range(len(nums)):
    nums[i] = int(nums[i])
 
for i in range(len(nums)):
    if s==nums[i]:
        print('Found',s,'at index', i)
        y = 1
if y == 0:
    print("No",s,"found.")