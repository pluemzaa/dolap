x = int(input("Enter a number N: "))
print(f"Prime numbers from 1 to {x} are:")
for i in range(2, x+1):
    if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
        print(i)