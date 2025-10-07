N = int(input("Enter the number of terms: "))
if N <= 0:
    print("Please enter a positive integer:")
elif N == 1:
    print("0")
else:
    a, b = 0, 1
    print(a, b, end=' ')
    for _ in range(2, N):
        t = a + b
        print(t, end=' ')
        a, b = b, t