nums1 = input("Enter numbers separated by commas: ")
nums1 = nums1.split(",")
nums2 = int(input("Enter number to search: "))

for i in range(len(nums1)):
    nums1[i] = int(nums1[i])
i = 0
if nums2 != nums1[i]:
    print("No", nums2, "found.")
else:
    for i in range(len(nums1)):
        if nums2 == nums1[i]:
            print("Found", nums2, "at index", i)