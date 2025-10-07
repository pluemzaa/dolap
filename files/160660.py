nums = input("Enter a series of numbers separated by commas: ")
nums =nums.split(",")

for i in range(len(nums)):                                                                                                                             
    nums[i] = int(nums[i])

min_value = min(nums)
max_value = max(nums)

x_scaled = [(num - min_value) / (max_value - min_value) for num in nums]
print(f"Normalized values:")
for value in x_scaled:
    print(f"{value:.2f}")