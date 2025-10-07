nums = list(map(int, input("Enter a series of numbers separated by commas: ").split(',')))
maximum = max(nums)
[print(f"{n} is the maximum value: {n == maximum}") for n in nums]