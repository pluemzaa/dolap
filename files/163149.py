A = int(input())
b = int(input())
c = int(input())

total = A * b

if total % c == 0:
    print(int(total/c))
else:
    print(int((total/c) + 1))