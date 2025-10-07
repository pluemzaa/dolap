nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])

Max = max(nums)
Min = min(nums)

if Max == Min:
    n = [0.0 for _ in nums]
else:
    n = [(x - Min) / (Max - Min) for x in nums]

print("Normalized values:")
for val in n:
    print(f"{val:.2f}")