nums = input("Enter numbers separated by commas: ")
se = input("Enter number to search: ")
nums = nums.split(",")
y = 10
i = 0
x = 0
while i < len(nums):
    nums[i] = int(nums[i])
    i = i+1
    #i+=1
i = 0
while i < len(nums):
    if y==nums[i]:
        print("Found",se, "at dex",i)
    if y==nums[x]:
        print("Found",se, "at dex",x)
        break  
    i+=1
    x+=1
else:
  print("No 10 found.")