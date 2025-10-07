nums = input().split(",")
nums = [int(i.strip()) for i in nums]

target = int(input())

found = False
for i in range(len(nums)):
    if nums[i] == target:
        print(f"Found {target} at index {i}")
        found = True

if not found:
    print(f"No {target} found")