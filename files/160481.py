nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
nums_search = input("Enter number to search: ")


for i in range(len(nums)):
    if nums_search==nums[i]:
       print("Found ",nums_search,"at index ",i)
if nums_search!=nums[i]:
       print("No ",nums_search," found.")