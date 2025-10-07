N = int(input("Enter the number of rows for the pyramid: "))
if 1 <= N <= 50:
    total_boxes = N * (N + 1) // 2
    print(f"The total number of boxes: {total_boxes}")
    # กรณีที่มันเป็น even number
    if total_boxes % 2 == 0:
        print("The total number of boxes is even")
        for i in range(1, N + 1):
            for j in range(i):
                print(i, end=' ')
            print()
        # กรณีที่มันเป็น odd number
    else:
        print("The total number of boxes is odd")
        for i in range(N, 0, -1):
            for j in range(i):
                print(i, end=' ')
            print()
else:
    print("Number of rows between 1 and 50.")