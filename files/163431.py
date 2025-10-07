N = int(input("Enter the number of rows for the pyramid: "))
if 1 <= N <= 50:
    total_boxes = N * (N + 1) // 2
    print(f"\nThe total number of boxes: {total_boxes}")

    if total_boxes % 2 == 0:
        print("The total number of boxes is even\n")
        for i in range(1, N + 1):
            print((str(i) + ' ') * i)
    else:
        print("The total number of boxes is odd\n")
        for i in range(N, 0, -1):
            print((str(i) + ' ') * i)
else:
    print("Invalid input. Please enter a number between 1 and 50.")