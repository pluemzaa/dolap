n = int(input("Enter number: "))

if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(n):  # แถว
        for j in range(n):  # คอลัมน์
            num = i * n + j + 1
            if num > 9:
                num = (num - 1) % 9 + 1  # ให้วนกลับเป็นเลข 1-9
            print(num, end=" ")
        print()  # ขึ้นบรรทัดใหม่หลังครบ 1 แถว