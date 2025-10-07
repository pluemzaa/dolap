nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

for i in range(0, len(nums)):
    nums[i] = int(nums[i])

y = int(input("Enter number to search: "))

found = False  # Flag to track if the number is found
for j in range(0, len(nums)):
    if y == nums[j]:
        print(f"Found {y} at index {j}")
        found = True
        break  # Exit the loop once the number is found

if not found:  # Check the flag after the loop completes
    print(f"No {y} found.")