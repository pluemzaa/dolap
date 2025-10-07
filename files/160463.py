nums = input("Enter numbers separated by commas:")
nums = nums.split(',')
search = input("Enter number to search:")

nums = [int(n) for n in nums]
search = int(search)

found = False

for i in range(len(nums)):
   if nums[i] == search:
       print(f"Found {search} at index {i}")
       found = True
    
if not found:
    print(f"NO {search} found.")