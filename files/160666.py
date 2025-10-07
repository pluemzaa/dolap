nums = (input("Enter a series of numbers separated by commas: "))
nums = nums.split(",")
for i in range(len(nums)):
    nums[i] = int(nums[i])
    
min_ = min(nums)
max_ = max(nums)

Normalized = [(i - min_) / (max_ - min_) for i in nums]
print("Normalized values: ")
for val in Normalized:
    print(f"{val:.2f}")