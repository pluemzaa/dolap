n = int(input("Enter the number of terms: "))
if n <= 0:
print("Please enter a positive integer.")
else:
    a, b = 0, 1
    for i in range(n):
        print(a, end='')
    a, b = b, a + b