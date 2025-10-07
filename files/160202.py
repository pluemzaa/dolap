nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(len(nums)):
      nums[i] = int(nums[i])

MAX = nums[0]
for i in range(len(nums)):
      if nums[i] > MAX:
            MAX = nums[i]
            print(f"set the maximum value to {MAX}")
            
print(f"The maximum value is {MAX}")