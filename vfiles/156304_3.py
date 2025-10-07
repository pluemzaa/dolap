nums = input("Enter a series of numbers separated by commas: ").split(',')
nums = [int(n) for n in nums]

maximum = max(nums)

[print(f"{n} is the maximum value: {n == maximum}") for n in nums]