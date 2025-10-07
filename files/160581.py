nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")

numtem = int(input("Enter number to search: "))

for i in range(len(nums)):
    nums[i] = int(nums[i])

found = False
for i in range(len(nums)):
    if numtem == nums[i]:
        print("Found", numtem, "at index", i)
        found = True

if not found:
    print("No", numtem, "found.")