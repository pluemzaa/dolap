nums = input("Enter numbers separated by commas:")
nums = nums.split(",")
nums1 = int(input("Enter number to search:"))
i = 0
for i in range(len(nums)):
    nums[i] = int(nums[i])

for i in range(len(nums)):
    if nums1 == nums[i]:
        print("Found",nums1,"at index",i)

if nums1 not in nums:
    print("No", nums1, "found.")