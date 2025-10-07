row = int(input("Enter the number of rows for the pyramid: "))
print(f"The total number of boxes: {(sum(range(1, row + 1)))}")
if 1 <= row <= 50 :
    if row % 2 == 0 :
        print("The total number of boxes is even")
        for i in range(1, row + 1):
            print(f"{i} " * i)  
        print('')
    elif row % 2 == 1 :
        print("The total number of boxes is odd")
        for i in range(row, 0, -1):
            print(f"{i} " * i)  
        print('')