# รับค่าจำนวนแถวของพีระมิด
N = int(input("Enter the number of rows for the pyramid: "))

# คำนวณจำนวนกล่องทั้งหมด (ผลรวม 1 + 2 + ... + N)
total_boxes = N * (N + 1) // 2

# แสดงจำนวนกล่องทั้งหมด
print("The total number of boxes:", total_boxes)

# ตรวจสอบว่าเป็นเลขคู่หรือเลขคี่
if total_boxes % 2 == 0:
    print("The total number of boxes is even")
    # แสดงพีระมิดแบบปกติ
    for i in range(1, N + 1):
        print((str(i) + " ") * i, end="")
        print()
else:
    print("The total number of boxes is odd")
    # แสดงพีระมิดแบบกลับหัว
    for i in range(N, 0, -1):
        print((str(i) + " ") * i, end="")
        print()