n = int(input("Enter number: "))
if n < 1:
    print("Error number must be 1 or greater")
i = j= 0
while i < n:
    j = 0
    while j < n:
        num = (i + j) % 9 + 1  
        print(num, end=' ')
        j += 1
    i += 1
    print()