nums=input('Enter numbers separated by commas: ')
nums=nums.split(',')
x=len(nums)

y=int(input('Enter number to search: '))

for i in range (x):
    nums[i]=int(nums[i])
    
for i in range (x):
    if y==nums[i] :
        print('Found ',y,' at index ',i)
   
print('No',y,' found.')