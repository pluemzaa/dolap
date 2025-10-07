# max check (แบบใช้ comparison + logical operators)

x = input("Enter a series of numbers separated by commas: ")
x = x.split(',')
y = list(map(int, x))

m = max(y)

print(y)

print(y[0], "is the maximum value:", y[0] == m)
print(y[1], "is the maximum value:", y[1] == m)
print(y[2], "is the maximum value:", y[2] == m)
print(y[3], "is the maximum value:", y[3] == m)
print(y[4], "is the maximum value:", y[4] == m)