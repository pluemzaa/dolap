nums = input("Enter numbers separated by commas:")
nums = nums.split(",")
y = int(input("Enter number to search:"))
z = 0
for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(len(nums)):
    if y ==nums[i]:
        print('Found',y,'at index',i)
        z=1


if z==0:
    print('No',y,'found.')