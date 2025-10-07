n = int(input("Enter the number of terms: "))
a = 0
b = 1
count = 0
print("Output:")
while count < n:
    print(a, end=" ")
    i = a + b
    a = b
    b = i
    count += 1