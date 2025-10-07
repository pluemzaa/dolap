v1_str = input("Enter v1 (space-separated):")
v1 = v1_str.split(" ")
v2_str = input("Enter v2 (space-separated):")
v2 = v2_str.split(" ")

# ตรวจสอบว่ามีแค่ 3 ตัว
if len(v1) != 3:
    print("Please enter exactly 3 numbers.")
else:
    # แปลงเป็นจำนวนเต็ม
    v1[0] = int(v1[0])
    v1[1] = int(v1[1])
    v1[2] = int(v1[2])
if len(v2) != 3:
    print("Please enter exactly 3 numbers.")
    v2[0] = int(v2[0])
    v2[1] = int(v2[1])
    v2[2] = int(v2[2])

    result = v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]
    print("Dot product:", result4)