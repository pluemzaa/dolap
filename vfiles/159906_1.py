def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
x = int(input("Enter a number N: "))
print("Prime numbers from 1 to", x, "are:")
for i in range(1, x + 1):
    if prime(i):
        print(i)