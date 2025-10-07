nums = input("Enter a series of numbers separated by commas: ").split(",")
nums = [int(n) for n in nums]
max_val = max(nums)
[print(f"{n} is the maximum value: {n == max_val}") for n in nums]