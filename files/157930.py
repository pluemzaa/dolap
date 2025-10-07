N = int(input("Enter a number N: "))
print("Prime numbers from 1 to", N, "are:")

for num in range(2, N + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)