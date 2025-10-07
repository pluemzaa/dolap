a = int(input("Enter number: "))
if  a<1 :
    print("Error number must be 1 or greater")\

for i in range(1, a + 1):
    for j in range(a):
        num = ((i + j - 1) % 9) + 1
        if num == 0:
            num = a
        print(num, end=' ')
    print()