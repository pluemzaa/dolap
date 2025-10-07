nums = input("Enter numbers separated by commas:")
nums = nums.split(",")

i = 0
y=int(input("Enter number to search:"))
for i in range(len(nums)):
    nums[i] = int(nums[i])
    i = i+1
    
i = 0
while i in range(len(nums)):
    if y==nums[i]:
        print("Found",y,"at index",i)
    i = i+1
else:
    print("No" ,y, "found.")