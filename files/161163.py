N = int(input("Enter the number of terms: "))

a, b = 0, 1
i = 0

while i < N:
    print(a, end=" ")
    a, b = b, a + b
    i =i+1