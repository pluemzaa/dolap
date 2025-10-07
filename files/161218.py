nums = input("Enter numbers seperated by comma: ")
nums = nums.split(",")
n = int(input("Enter number to search: "))
for i in range(len(nums)):
    nums[i] = int(nums[i])
for i in range(len(nums)):
    if n==nums[i]:
        print(f"found {n} at index {i}")
    elif n not in nums:
        print(f"No {n} found.")
        break