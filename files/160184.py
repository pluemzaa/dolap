nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")

nor = 0.0

for i in range(len(nums)):
    nums[i] = int(nums[i])

Max = nums[0]
for i in range(len(nums)):
    if nums[i] > Max:
        Max = nums[i]

Min = nums[0]
for i in range(len(nums)):
    if nums[i] < Min:
        Min = nums[i]

print("Normalized values:")

for i in range(len(nums)):
    x = nums[i]
    nor = (x-Min)/(Max-Min)
    print(f"{nor:.2f}")