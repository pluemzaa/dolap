numbers = input("Enter a series of numbers separated by commas: ")
nums = [int(n) for n in numbers.split(",")]
max_number = max(nums)
results = [n == max_number for n in nums]

for n, is_max in zip(nums, results):
    print(f"{n} is the maximum value: {is_max}")