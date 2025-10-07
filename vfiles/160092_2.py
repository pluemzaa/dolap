n=int(input("Enter a number N:"))
print(f"Prime number from 1 to {n} are:")
for i in range(2,n):
    for j in range(2, int(i ** 0.5) + 1):
        if i%j== 0: break
    else:
        print(i)