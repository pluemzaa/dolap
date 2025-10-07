nums = input("Enter a series of numbers separated by commas: ")
nums = [int(x) for x in nums.split(",")]
max_val = max(nums)
for num in nums:
    print(f"{num} is the maximum value: {num == max_val}")