nums = list(int,input("Enter a series of numbers separated by commas:").split(',')))
maximum_value = max(nums)
for n in nums:
    print(f"{n} is the maximum value:{n == maximum_value}")