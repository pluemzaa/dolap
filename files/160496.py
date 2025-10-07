nums = input("Enter numbers separated by commas:")
nums = nums.split(",")
num = int(input("Enter number to search:"))
y = 0
for i in range(len(nums)):
        nums[i] = int(nums[i])

for i in range(len(nums)):
    if num==nums[i]:
        print('Found',num,'at index', i)
        y = 1
        
if y == 0:
     print("No",num,"found.")