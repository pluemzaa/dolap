nums = input("Enter numbers separated by commas:")
numx = int(input("Enter number to search:"))
nums = nums.split(",")
i = 0
found = False
for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(len(nums)):
    if numx==nums[i]:
        print("Found",numx, "at index ",i)
        found = True

if not found:
    print("No",numx, "found.")