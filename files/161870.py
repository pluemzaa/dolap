n = int(input("Enter number: "))
if n < 1:
    print("Error number must be 1 or greater")

i = 0
while i < n:
    j = 0
    while j < n:
        print(((i + j) % 9) + 1, end=' ')
        j += 1
    print()
    i += 1