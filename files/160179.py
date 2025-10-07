nums_input = input("Enter numbers separated by commas: ")
nums = nums_input.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])


sn = int(input("Enter number to search: "))


found = False
for i in range(len(nums)):
    if nums[i] == sn:
        print(f"Found {sn} at index {i}")
        found = True

if not found:
    print(f"No {sn} found.")