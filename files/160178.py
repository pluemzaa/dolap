nums = input("Enter numbers separated by commas: ").split(',')
s = int(input("Enter number to search: "))
for i in range(len(nums)):
    nums[i] = int(nums[i])
    
for i in range(len(nums)):  
    if s == nums[i]:
        print("Found",nums[i] ,'at index',i)              
    else:
        print("No",s,"found.")
        break