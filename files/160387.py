nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(',')
Nuorm = 0

for i in range (0,len(nums)):
    nums[i] = int(nums[i])

print ("Normalized values:")

for i in range(len(nums)):
    Nuorm = (nums[i]- min(nums)) / (max(nums) - min(nums))
    print(f"{Nuorm:.2f}")