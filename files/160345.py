nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
nums1 =input("Enter number to search: ")
for i in range(0, len(nums)):
        nums[i] = int(nums[i])
found = False
for i in range(0, len(nums)):
    if int(nums1) == nums[i]:
        print("Found", nums1, "at index", i)
        found = True
if not found:
    print("No", nums1, "found.")