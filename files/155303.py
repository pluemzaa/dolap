nums = input("Enter a series of numbers separated by commas: ").split(",")
for i in range(5):
    nums[i] = int(nums[i])

minN = min(nums)
maxN = max(nums)
print("Normalized values:")
for num in nums:
    print("%.2f" %((num-minN)/(maxN-minN)))