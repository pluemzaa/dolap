i = 0
nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
y = int(input("Enter number to search: "))
while i < len(nums):
    nums[i] = int(nums[i])
    i += 1
i = 0
while i < len(nums):
    if y == nums[i]:
        print(f"Found {y} at index {i}")
    elif y != nums[i]:
        wa = f"No {y} found."
    i += 1

print(wa)