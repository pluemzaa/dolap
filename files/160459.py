nums = input("Enter numbers separated by commas:")
nums = nums.split(",")
numb = int(input("Enter number to search: "))
s = 0
for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(len(nums)):
    if numb==nums[i]:
        print('Found',numb,'at index ',i)  
        s = 1
if s==0:
    print('No',numb,'found.')