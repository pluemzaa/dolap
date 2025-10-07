print("===== Calculate Grade Program =====")
student = []
g = []
count = 1
while True :
    name = input(f"Enter student name No.{count} : ")
    grade = float(input("Enter Grade : "))
    student.append(name)
    g.append(grade)
    
    cont = input("Continue? (y/n) : ")
    if cont == 'y' :
        count +=1
    elif cont == 'n':
        break
total = sum(g)
avg = total / len(g)
max_index = g.index(max(g))
min_index = g.index(min(g))
    
print("\n===== Report =====")
print(f"Average : {avg:.2f}")
print(f"Max : ",student[max_index])
print(f"Min : ",student[min_index])