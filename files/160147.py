nums = input("Enter numbers separated by commas:")
serch = int(input("Enter number to search:"))
nums = nums.split(",")
y=0


i=0
while i < len(nums):
    nums[i] = int(nums[i])
    if serch==nums[i]:
        print("Found ",serch,"at  index ",i)
        y+=1
    i+=1
        
if y ==0:
    print("No",serch,"found.")