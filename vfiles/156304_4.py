nums = [int(input(f"Enter a series of numbers separated by commas: ")) for i in range(5)]
maximum = max(nums)
results = [num == maximum for num in nums]
for i, result in enumerate(results):
    print(f"Enter a series of numbers separated by commas: => {result}")