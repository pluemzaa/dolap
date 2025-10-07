nums = input("Enter numbers separated by commas:")
nums = nums.split(",")
num = int(input("Enter number to search:"))
i = 0
  
while i<len(nums):
    nums[i] = int(nums[i])
    i+=1
i = 0
while i<len(nums):
    if num==nums[i]:
        print("Found",num,"at index:",i,)
    i =i+1
    break
i = 0
while i<len(nums):
    if num!=nums[i]:
        print("No",num,"found.")
        break