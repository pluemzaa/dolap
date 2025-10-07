nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])
min_n = min(nums)
max_n = max(nums)

# ใส่เงื่อนไขกรณี max_n == min_n
if max_n == min_n:
    x_scaled = [0 for _ in nums]
else:
    x_scaled = [(x - min_n)/(max_n - min_n) for x in nums]

print("Normalized values:")
for value in x_scaled:
    print(""f"{value:.2f}")