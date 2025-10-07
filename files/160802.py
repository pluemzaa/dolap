nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")
for i in range(len(nums)):
    nums[i] = float(nums[i])
min_val = min(nums)
max_val = max(nums)
if max_val == min_val:
    print("Normalized values: ")
    for i in nums:
        print("0.00")
else:
    print("Normalized values: ")
    for x in nums:
        x_scaled = (x - min_val)/(max_val - min_val)
        print(f"{x_scaled:.2f}")