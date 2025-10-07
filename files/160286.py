a = input("Enter a series of numbers separated by commas: ")
nums = a.split(",")

max = nums[0]
for i in range(len(nums)):
    if nums[i] > max:
        max = nums[i]
        print(f"set the maximum value to {max}")


print("The maximum value is",max)