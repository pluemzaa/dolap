nums_input = input("Enter a series of numbers separated by commas: ")
nums = [int(num.strip()) for num in nums_input.split(",")]

max = nums[0]

for i in nums[1:]:
    if i > max:
        max = i
        print(f"set the maximum value to {max}")

print(f"The maximum value is {max}")