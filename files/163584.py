# รับค่าจำนวนชั้นของพีระมิด
N = int(input("Enter the number of rows for the pyramid: "))

# ตรวจสอบเงื่อนไขขอบเขต
if N < 1 or N > 50:
    print("Invalid input! N must be between 1 and 50.")
    exit()

# คำนวณจำนวนกล่องทั้งหมด
total_boxes = N * (N + 1) // 2

# แสดงจำนวนกล่องทั้งหมด
print(f"The total number of boxes: {total_boxes}")

# ตรวจสอบเลขคู่หรือเลขคี่
if total_boxes % 2 == 0:
    print("The total number of boxes is even")
    # แสดงพีระมิดแบบปกติ
    for i in range(1, N + 1):
        print(" ".join([str(i)] * i))
else:
    print("The total number of boxes is odd")
    # แสดงพีระมิดแบบกลับหัว
    for i in range(N, 0, -1):
        print(" ".join([str(i)] * i))