P = int(input("Enter the number of rows for the pyramid: "))
total = P * (P + 1)//2
if P % 2 == 0:
    print(f"The total number of boxes: {total}")
    print("The total number of boxes is even")
    for i in range(1, P+1):
        print(*([i] * i))
elif P % 2 != 0 :
    print(f"The total number of boxes: {total}")
    print("The total number of boxes is odd")
    for i in range(P, 0, -1):
        print(*([i] * i))