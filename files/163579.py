a = int(input("Enter the number of rows for the pyramid: "))
if 1 <= a <= 50:
    b = a * (a + 1) // 2
    print("The total number of boxes:",b)
    
    if b % 2 == 0:
        print("The total number of boxes is even")
        for i in range(1, a + 1):
            for j in range(i):
                print(i, end=" ")
            print()
    else:
        print("The total number of boxes is odd")
        for i in range(a, 0, -1):
            for j in range(i):
                print(i, end=" ")
            print()
else:
    pass