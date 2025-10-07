mN = int(input("Enter the number of rows for the pyramid: "))

total_boxes = N * (N + 1) // 2


print(f"The total number of boxes: {total_boxes}")

if total_boxes % 2 == 0:
    print("The total number of boxes is even")
    for i in range(1, N + 1):
        for j in range(i):
            print(i, end=" ")
        print()
else:
    print("The total number of boxes is odd")
    for i in range(N, 0, -1):
        for j in range(i):
            print(i, end=" ")
        print()