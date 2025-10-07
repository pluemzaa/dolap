nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
nbs = int(input("Enter number to search: "))


for i in range(0,len(nums)):
    nums[i] = int(nums[i])
        

for i in range(0,len(nums)):
    if nbs == nums[i]:
        print("Found",  nbs, "at index",i)
for i in range(1,len(nums)):
    if nbs == nums[i>0]:
        print("Found",  nbs, "at index",i>0)
    
else:
    print("No",nbs,"found.")