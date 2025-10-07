nums = input("Enter number:")
nums = nums.split(",")
n = len(nums)

for i in range(len(n)):
    nums[i] = int(nums[i])

avg = sum(nums)/len(n)
s = 0
for i in range(n):
    s = s + (nums[i]-avg)**2

    s = s/(n-1)
    sd = s**0.5
    print ('SD=' , sd)