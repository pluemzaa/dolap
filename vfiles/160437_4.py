nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")

i = 0
for i in range(len(nums)):
    nums[i]=int(nums[i])
    
s = int(input("Enter number to search: "))
index = 0

for i in range(len(nums)):
    if nums[i] == s:
      print('Found', s ,' at index ', i)
      index =+1
  
if index == 0:
    print(f"No {s} found")