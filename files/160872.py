nums = input("Enter a series of numbers separated by commas:")
nums = nums.split(",")
for i in range(len(nums)):
    nums[i] = int(nums[i])

max = nums[0]
min = nums[0]
for i in range(len(nums)):
    if nums[i]>max:
        max=nums[i]
for i in range(len(nums)):
    if nums[i]<min:
        min=nums[i]
print("Normalized values:")
x = 0
for i in range(len(nums)):
    x = (nums[i]-min)/(max-min)
    print(f"{x:.2f}")