nums = input("Enter numbers separated by commas:").split(",")
y = int(input("Enter number to search:"))
#cast str -> int
i = 0
for i in range(len(nums)):
    nums[i] = int(nums[i])

i = 0
for i in range(len(nums)):

    if y in nums:
        if y ==nums[i]:
    else:
        print(f"Found {y} at index {i}")
        break