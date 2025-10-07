nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")
for i in range(len(nums)):
    nums[i] = float(nums[i])
minimum = min(nums)
maximum = max(nums)
print("Normalized values:")
for i in nums:
    normalized = (i - minimum) / (maximum - minimum)
    print(f"{normalized:.2f}")