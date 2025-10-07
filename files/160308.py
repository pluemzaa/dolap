n = input("Enter a series of numbers separated by commas: ")
n = n.split(",")
l = len(n)
for a in range(l):
    n[a] = int(n[a])

m = n[0]

for i in range(l):
    if m < n[i]:
        print(f"set the maximum value to {n[i]}")
        m = n[i]
print(f"The maximum value is {m}")