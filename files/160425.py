a = input("Enter a series of numbers separated by commas: ")
nums = a.split(",")

max = int(nums[0])  

for i in range(len(nums)):
    nums[i] = int(nums[i])
    if nums[i] > max:
        max = nums[i]
        print(f"set the maximum value to {max}")

print("The maximum value is", max)