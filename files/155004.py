num_text = input("Enter a series of numbers separated by commas: ")
num = num_text.split(",")
num[0] = int(num[0])
num[1] = int(num[1])
num[2] = int(num[2])
num[3] = int(num[3])
num[4] = int(num[4])
x_max = int(max(num))
r0 = num[0]
r1 = num[1]
r2 = num[2]
r3 = num[3]
r4 = num[4]

print(f"{r0} is the maximum value:", r0 == x_max)
print(f"{r1} is the maximum value:", r1 == x_max)
print(f"{r2} is the maximum value:", r2 == x_max)
print(f"{r3} is the maximum value:", r3 == x_max)
print(f"{r4} is the maximum value:", r4 == x_max)