nums = list(map(int,input("Enter a series of numbers separated by commas:").split(',')))
max_value = max(nums)
for n in nums:
    print(f"{n} is the maximum value:{n == max_value}")