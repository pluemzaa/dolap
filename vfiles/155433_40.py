num = input("Enter a series of numbers separated by commas:")
n = num.split(",")

n1 = int(n[0])
n2 = int(n[1])
n3 = int(n[2])
n4 = int(n[3])
n5 = int(n[4])

max_value = max(num)

print(n[0], " is the maximum value:", n[0] == max_value)
print(n[1], " is the maximum value:", n[1] == max_value)
print(n[2], " is the maximum value:", n[2] == max_value)
print(n[3], " is the maximum value:", n[3] == max_value)
print(n[4], " is the maximum value:", n[4] == max_value)