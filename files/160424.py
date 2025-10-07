nums = input("Enter a series of numbers separated by commas: ")
nums = [int(x) for x in nums.split(",")]

maxx = nums[0]
for n in nums[1:]:
    if n > maxx:
        maxx = n
        print("set the maximum value to ",maxx)
print("The maximum value is ",maxx)