n= int(input('Enter the number of terms:'))
a = 0
b = 1
for i in range (n):
    if n >= 0:
        print(a,end=" ")
        a, b = b, a + b