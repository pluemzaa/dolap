n = int(input("Enter number: "))

if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(n):  # i คือลำดับแถว เริ่มจาก 0
        for j in range(n):  # j คือลำดับหลักในแต่ละแถว
            num = (i + j + 1)  # เริ่มจาก i+1 แล้วเพิ่มไปเรื่อยๆ
            if num > 9:
                num = (num - 1) % 9 + 1  # ทำให้วนกลับมาเป็น 1-9
            print(num, end=" ")
        print()