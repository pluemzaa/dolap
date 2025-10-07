N = int(input("Enter a number N:"))
print(f'Prime number from 1 to {N} are:')
for i in range(2,N+1):
    prime = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            prime = False
            break
    if prime:
     print(i)