nums = list(map(int, input("Enter a series of numbers separated by commas: ").split(",")))
maximum = max(nums)
results = [(str(n) + " is the maximum value: " + str(n == maximum)) for n in nums]
print("\n".join(results))