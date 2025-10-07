nums_input = input("Enter a series of numbers separated by commas:")
nums = [int(x.strip()) for x in nums_input.split(",")]

maximum = nums[0]

for num in nums [1:]:
    if num> maximum:
        maximum = num
        print(f"set themaximum value to {maximum}")
        
print(f"The maximum value is {maximum}")