rows = int(input("Enter the number of rows for the pyramid: "))

list = []

n = 0
a = ""

if rows >= 1 and rows <= 50:
    if rows % 2 == 0:
        a = "even"
    else:
        a = "odd"

    for i in range(rows):
        list.append([])
        
        for j in range(i + 1):
            list[i].append(i + 1)
            
            n +=1
            
    print(f"The total number of boxes: {n}") 
    print(f"The total number of boxes is {a}") 
            
    for k in range(len(list)):
        if a == "odd":
            k = len(list) - k - 1
        
        v = list[k]
        
        for h in range(len(v)):
            print(v[h],end = " ")
            
        print("")