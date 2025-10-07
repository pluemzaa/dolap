N = int(input("Enter the number of rows for the pyramid: "))

total_boxes = sum(range(1, N + 1))

print(f"\nThe total number of boxes: {total_boxes}")

if total_boxes % 2 == 0:
    print("The total number of boxes is even")
    for i in range(1, N + 1):
        print((str(i) + ' ') * i)
else:
    print("The total number of boxes is odd")
    for i in range(N, 0, -1):
        print((str(i) + ' ') * i)