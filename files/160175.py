nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
y = int(input("Enter number to search: "))
i = 0
while i < len(nums):
    nums[i] = int(nums[i])
    i = i + 1
i = 0
found = False
while i < len(nums):
    if y == nums[i]:
        print("Found", y, "at index", i)
        found = True
    i += 1
if not found:
    print("No", y, "found.")