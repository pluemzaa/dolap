nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")
for i in range(len(nums)):
    nums[i] = int(nums[i])
Max=max(nums)
Min=min(nums)
print("Normalized values:")
for i in nums:
    print(f"{(i - Min) / (Max - Min):.2f}")