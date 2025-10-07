nums = input("Enter a series of numbers separated by commas: ")
nums = [float(n.strip()) for n in nums.split(",")]

max_val = None

for num in nums:
    if max_val is None or num > max_val:
        max_val = num
        print(f"set the maximum value to {max_val:.0f}")

print(f"The maximum value is {max_val:.0f}")