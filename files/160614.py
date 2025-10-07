numbers = input("Enter a series of numbers separated by commas: ")
nums = [float(x.strip()) for x in numbers.split(",")]

min_v = min(nums)
max_v = max(nums)

print("Normalized values:")
for num in nums:
    if max_v != min_v:
        normalized = (num - min_v) / (max_v - min_v)
    else:
        normalized = 0.
    print(f"{normalized:.2f}")