nums = input("Enter numbers separated by commas: ")
nums = nums.split(',')
Nuorm = 0

for i in range (0,len(nums)):
    nums[i] = int(nums[i])

print ("Normalized values:")

for i in range(len(nums)):
    if nums[i] > 0:
        Nuorm = (nums[i]- min(nums)) / (max(nums) - min(nums))
        print(Nuorm)