nums=input("Enter numbers separated by commas: ")
nums=nums.split(",")
se=int(input("Enter number to search: "))

for i in range(0,len(nums)):
    nums[i]=int(nums[i])

for i in range(0,len(nums)):
    if se==nums[i]:
         print('Found',se,'at index',i)
if se not in nums:
     print("No",se,"found.")