n = int(input("Enter number: "))
if n < 1:
    print("Error: number must be 1 or greater")
else:
    for i in range(1, n + 1):  # i คือขั้นที่
        if i == 1:
            stars = 2
        else:
            stars = 2 * i + 1
        for j in range(2):  # พิมพ์ 2 บรรทัดต่อขั้น
            print('*' * stars)