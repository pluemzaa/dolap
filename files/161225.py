nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")
for i in range(len(nums)):
    nums[i] = float(nums[i])

mn = min(nums)
mx = max(nums)

print("Normalized values:")
for n in nums:
    if mx - mn == 0:
        print("0.00")
    else:
        val = (n - mn) / (mx - mn)
        print("%.2f" % val)