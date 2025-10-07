a = input("Enter input: ")
b = len(a)
sum = ""
for i in range(b-1, -1, -1):
    sum += a[i]
print(sum)