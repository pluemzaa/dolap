nums1 = input("Enter numbers separated by commas: ")
nums1 = nums1.split(",")
nums2 = int(input("Enter number to search: "))

for i in range(len(nums1)):
    nums1[i] = int(nums1[i])
    
for j in range(len(nums1)):
    if nums2 == nums1[j]:
        print("Found", nums2, "at index", j)
    elif nums2 not in nums1:
        print("No",nums2 ,"found")