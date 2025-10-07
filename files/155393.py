nums_text = input("Enter a series of numbers separated by commas:")
nums = nums_text.split(",")
nums1 = int(nums[0])
nums2 = int(nums[1])
nums3 = int(nums[2])
nums4 = int(nums[3])
nums5 = int(nums[4])

nums_list = [nums1,nums2,nums3,nums4,nums5]
_max = max(nums_list)

print(f"{nums1} is the maximum value:", nums1 is _max)
print(f"{nums2} is the maximum value:", nums2 is _max)
print(f"{nums3} is the maximum value:", nums3 is _max)
print(f"{nums4} is the maximum value:", nums4 is _max)
print(f"{nums5} is the maximum value:", nums5 is _max)