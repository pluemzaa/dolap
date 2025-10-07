n = int(input("Enter the number of rows for the pyramid: "))

total_ = n * (n + 1) // 2


print(f"The total number of boxes: {total_}")

if total_ % 2 == 0:
    print("The total number of boxes is even")
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()
else:
    print("The total number of boxes is odd")
    for i in range(n, 0, -1):
        for j in range(i):
            print(i, end=" ")
        print()