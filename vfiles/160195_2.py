nums = input("Enter numbers separated by commas: ")
find_nums = int(input("Enter number to search: "))
nums = nums.split(",")
i = 0
while i < len(nums):
    nums[i] = int(nums[i])
    i = i + 1
i = 0
while i < len(nums):
    if find_nums==nums[i]:
        print("Found",find_nums,"at index",i)       
    i += 1 
if find_nums != nums:
    print("No",find_nums,"found.")