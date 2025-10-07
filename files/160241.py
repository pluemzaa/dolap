nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")

for i in range(len(nums)):
      nums[i] = int(nums[i])
      
nmax = max(nums)
nmin = min(nums)

print("Normalized values: ")
for i in range(len(nums)):
      cal = (nums[i]-nmin)/(nmax-nmin)
      print(f"{cal:.2f}")