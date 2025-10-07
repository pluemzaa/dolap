n = int(input("Enter a number: "))

if n < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(1, n+1):  # แถว
        for j in range(i, i+n):  # ค่าที่จะพิมพ์ในแต่ละแถว
            num = j
            if num > 9:
                num = (num - 1) % 9 + 1  # วนกลับมาเป็น 1
            print(num, end=" ")
        print()