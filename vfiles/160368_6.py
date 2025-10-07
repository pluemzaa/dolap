nums = input().split(",")
nums = [int(x.strip()) for x in nums]

maximum = nums[0]
print(f"set the maximum value to {maximum}")

for i in nums[1:]:
    if i > maximum:
        maximum = i
        print(f"set the maximum value to {maximum}")

print(f"The maximum value is {maximum}")