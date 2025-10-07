e_san = int(input("Enter number:"))

if e_san < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(e_san):
        for j in range(e_san):
            print(((i+j)%9)+1, end=" ")
        print()