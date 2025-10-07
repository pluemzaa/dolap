nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])

min_val = min(nums)
max_val = max(nums)

print("Normalized values:")
for i in range(len(nums)):
    if max_val - min_val == 0:
        normalized = 0
    else:
        normalized = (nums[i] - min_val) / (max_val - min_val)
    print(f"{normalized:.2f}")