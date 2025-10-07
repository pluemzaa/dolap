nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i]) 

x_min = min(nums)
x_max = max(nums)

print("Normalized values:")
for num in nums:
    done = (num - x_min) / (x_max - x_min)
    print(f"{done:.2f}")