nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])

min = min(nums)
max = max(nums)

if max == min :
    n = [0.0 for _ in nums]
else :
    n = [(x-min)/(max-min) for x in nums]

print("Normalized values: ")
for val in n:
    print(f"{val:.2f}")

sx =0
for i in range(len(nums)):
    sx = sx-min
sx = sx/(max-min)