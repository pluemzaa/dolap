import sys

n = int(input("Enter Number :"))

if n < 1:
    print("Error number must be 1 or greater")
    sys.exit()

for i in range(1,n+1):
    for j in range(n):
        numbers = (i + j - 1 ) % 9 + 1
        print(numbers,end = " ")
    print()