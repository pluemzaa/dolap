print("===== Calculate Grade Program =====")
lst = []
lsg = []
i=0
while True:
    i +=1
    lst.append(input(f"Enter student name No.{i} :"))
    lsg.append(float(input('Enter Grade :')))
    yn = input("Continue? (y/n) :")
    if lst[i] > lst[i-2]:
        iMax = i
    if lst[i] < lst[i-2]:
        iMin = i
    if yn == 'n' :
        print("===== Report =====")
        break
print()    
print(f"Average : {(sum(lsg)/len(lsg)):.2f}")
print(f"Max :  {lst[lsg.index(max(lsg))]}")
print(f"Min :  {lst[lsg.index(min(lsg))]}")