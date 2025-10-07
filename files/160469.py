nums=input("Enter numbers separated by commas:")
nums=nums.split(",")
x=input("Enter number to search:")

for i in range(len(nums)):
    if x==nums[i]:
        print('Found',x,'at index',i)

y=0
for i in range(len(nums)):
    if y!=nums[i]:
        print('No',x,'found.')
        break