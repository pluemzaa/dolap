n = int(input("Enter a number N: "))

print("Prime numbers from 1 to", n, "are:")

for num in range(2, n + 1):
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)