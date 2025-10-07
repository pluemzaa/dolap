primeN = 1
N = int(input("Enter a number N: "))
print("Prime numbers from", primeN, "to", N, "are:")
for num in range(primeN, N + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)