n = int(input("Enter the number of terms: "));a = 0;b = 1
for i in range(n):
    print(a, end=' ')
    next_num = a + b
    a = b
    b = next_num
print()