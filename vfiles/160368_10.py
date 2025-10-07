print("Enter a series of numbers separated by commas:", end=" ")
input_str = input()
nums = [int(x.strip()) for x in input_str.split(",")]

maximum = nums[0]

for i in nums[1:]:
    if i > maximum:
        maximum = i
        print(f"set the maximum value to {maximum}")
        print(f"The maximum value is {maximum}")