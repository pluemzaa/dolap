nums_str = input("Enter a series of numbers separated by commas: ")

nums = [int(n) for n in nums_str.split(',')]

min_v = min(nums)
max_v = max(nums)

print("Normalized values:")

if max_v == min_v:
    for _ in nums:
        print(f"{0.00:.2f}")
else:
    for num in nums:
        scaled_n = (num - min_v) / (max_v - min_v)
        print(f"{scaled_n:.2f}")