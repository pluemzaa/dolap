x=int(input("Enter a number N: "))
print("Prime numbers from 1 to {} are:".format(x))
for num in range(2,x+1):
    is_prime=True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime=False
    if is_prime:
        print(num)