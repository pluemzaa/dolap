num = input("Enter a series of numbers separated by commas: ")
nums = num.split(',')
x1 = int(nums[0])
x2 = int(nums[1])
x3 = int(nums[2])
x4 = int(nums[3])
x5 = int(nums[4])
max = int(max(nums))
y1 = x1 == max
y2 = x2 == max
y3 = x3 == max
y4 = x4 == max
y5 = x5 == max
print(f"{x1} is the maximum value: {y1}")
print(f"{x2} is the maximum value: {y2}")
print(f"{x3} is the maximum value: {y3}")
print(f"{x4} is the maximum value: {y4}")
print(f"{x5} is the maximum value: {y5}")