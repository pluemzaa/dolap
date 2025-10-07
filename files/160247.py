nums = input("Enter numbers:")
nums = nums.split(",")
y =- 10
#cast str -> int
#nums[0] = int(nums[0])
#nums[1] = int(nums[1])
#nums[2] = int(nums[2])
i = 0
while i < len(nums):
    nums[i] = int(nums[i])
    i = i+1
i = 0
while i < len(nums):
    if y==nums[i]:
        print("Fount at indax")
        break
    i+=1
    
print(nums)