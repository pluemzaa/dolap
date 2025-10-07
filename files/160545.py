nums = input("Enter a series of numbers separated by commas: ").split(",")

for i in range(len(nums)):
    nums[i] = int(nums[i])

Max = max(nums)
Min = min(nums)
x = 0
print("Normalized values:")
for i in range(len(nums)):
    x = (nums[i]-Min)/(Max-Min)
    print(f'{x:.2f}')