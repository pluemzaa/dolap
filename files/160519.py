nums = input("Enter numbers separated by commas:")
search = int(input("Enter number to search: "))
nums = nums.split(",")
f=0

for i in range(len(nums)):
    nums[i]= int(nums[i])

for i in range(len(nums)):
    if search ==nums[i]:
        print('Found',search ,'at index',i)
        f=1


else: f==0
print('No' ,search, 'found.')