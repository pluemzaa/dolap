nums_text = input("Enter a series of numbers separated by commas: ")

nums = [float(num.strip()) for num in nums_text.split(",")]

x_min = min(nums)
x_max = max(nums)

if x_max == x_min:
    normalized = [0.00 for _ in nums]  
else:
    normalized = [(x - x_min) / (x_max - x_min) for x in nums]

print("Normalized values:")
for val in normalized:
    print("%.2f" % val)