rows =  int(input("Enter the number of rows for the pyramid:"))

total_boxes = (rows * (rows + 1)) // 2
print(f"The total number of boxes: {total_boxes}")
if rows >= 1 and rows <= 50:
    if total_boxes % 2 == 0:
        print("The total number of boxes is even")
        for i in range(1,rows + 1):
            print((str(i) + " ") * i)

    else:
        print("The total number of boxes is odd")
        for i in range(rows, 0, - 1):
            print((str(i) + " ") * i)