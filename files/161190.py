nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])
min_ = min(nums)
max_ = max(nums)
if max_ == min_:
    x_scaled = [0 for _ in nums]
else:
    x_scaled = [(x - min_)/(max_ - min_) for x in nums]

print("Normalized values:")
for value in x_scaled:
    print(""f"{value:.2f}")