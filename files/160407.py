nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",") 
N = 0
for i in range(0,len(nums)):
    nums[i] = int(nums[i])

Max = nums[0]
for i in range(len(nums)):
    if nums[i] > Max:
        Max = nums[i]

Min = nums[0]
for i in range(len(nums)):
    if nums[i] < Min:
        Min = nums[i]
print('Normalized values:')

for i in range(len(nums)):
    x = nums[i]
    N = (x-Min)/(Max-Min)
    print(f"{N:.2f}")