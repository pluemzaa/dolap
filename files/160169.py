nums = input("Enter numbers separated by commas:")
nums = nums.split(",")
for i in range(len(nums)):
    nums[i] = int(nums[i])

x = int(input("Enter number to search:"))


for i in range(len(nums)):   
    if x == nums[i] :
        print(f"Found {nums[i]:} at index {i:}") 
            
print(f"No {x:} found.")