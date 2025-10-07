row = int(input("Enter the number of rows for the pyramid: "))
s = 0
if 1 <= row <= 50:
    if row%2==0:
        for i in range(1,row+1):
                s+=1*i
        if s%2==0:
                print(f"The total number of boxes: {s}")
                print("The total number of boxes is even")
                for i in range(1,row+1):
                        print(f'{i} '*i)
        else :
                print(f"The total number of boxes: {s}")
                print("The total number of boxes is odd")
                for i in range(1,row+1):
                        print(f'{i} '*i)
    else :
        for i in range(row,0,-1):
                s+=1*i
        if s%2==0:
                print(f"The total number of boxes: {s}")
                print("The total number of boxes is even")
                for i in range(row,0,-1):
                        print(f'{i} '*i) 
        else :
                print(f"The total number of boxes: {s}")
                print("The total number of boxes is odd")
                for i in range(row,0,-1):
                        print(f'{i} '*i)