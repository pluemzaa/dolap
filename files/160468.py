nums = input("Enter numbers separated by commas:")
ns = int(input("Enter number to search: "))
nums = nums.split(",")
c=0

i=0
while i < len(nums):
    nums[i] = int(nums[i])
    if ns == nums[i]:
        print("Found",ns,"at index",i)
        c+=1
    i+=1    
    
if c==0:
    print("No",ns,"found.")