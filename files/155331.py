num = input("Enter a series of numbers separated by commas:").split(",")
for i in range(5):
    num[i] = int(num[i])

numx = max(num)
r0 = num[0] == numx
r1 = num[1] == numx
r2 = num[2] == numx
r3 = num[3] == numx
r4 = num[4] == numx

print(f"{num[0]} is the maximum value:{r0}")
print(f"{num[1]} is the maximum value:{r1}")
print(f"{num[2]} is the maximum value:{r2}")
print(f"{num[3]} is the maximum value:{r3}")
print(f"{num[4]} is the maximum value:{r4}")