print("===== Calculate Grade Program =====")
lst = []
lsg = []
i=0
while True:
    i +=1
    lst.append(input(f"Enter student name No.{i} :"))
    lsg.append(float(input('Enter Grade :')))
    yn = input("Continue? (y/n) :")
    if lst[i] > lst[i-1]:
        iMax = i
    if lst[i] < lst[i-1]:
        iMin = i
    if yn == 'n' :
        print("===== Report =====")
        break
    
print(f"Average : {(sum(lsg)/len(lsg)):.2f}")
print(f"Max :  {lst[iMax]}")
print(f"Min :  {lst[iMin]}")