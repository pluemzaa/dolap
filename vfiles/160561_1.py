nums = input("Enter number: ")
nums = nums.split(",")
l = len(nums)
for i in range(l):
    nums[i] = int(nums[i])
    
avg = sum(nums)/l
s = 0
for i in range(l):
    s = s + (nums[i]-avg)**2
    
s = s/(l-1)
sd = s**0.5
print('SD =', sd)