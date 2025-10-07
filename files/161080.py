print("Enter a series of numbers separated by commas: ", end="")
user_input = input()
nums_str = user_input.split(",")
nums = []
i = 0
while i < len(nums_str):
    nums.append(float(nums_str[i]))
    i += 1

min_val = nums[0]
i = 1
while i < len(nums):
    if nums[i] < min_val:
        min_val = nums[i]
    i += 1

max_val = nums[0]
i = 1
while i < len(nums):
    if nums[i] > max_val:
        max_val = nums[i]
    i += 1

print("Normalized values:")
i = 0
while i < len(nums):
    if max_val == min_val:
        scaled = 0.0
    else:
        scaled = (nums[i] - min_val) / (max_val - min_val)
    print(f"{scaled:.2f}")
    i += 1