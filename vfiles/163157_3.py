print("===== Calculate Grade Program =====")
list_name = []
list_grade =[]
i = 0
while True:
    i += 1
    name = input(f"Enter student name No.{i}: ")
    list_name.append(name)
    
    grade = float(input("Enter Grade : "))
    list_grade.append(grade)
    
    con = input("Continue? (y/n) : ")
    if con.lower() == 'n':
        break
    
average = sum(list_grade) / len(list_grade)

max_grade = max(list_grade)
min_grade = min(list_grade)

max_index = list_grade.index(max_grade)
min_index = list_grade.index(min_grade)

print("===== Report =====")
print(f"Average :{average:.2f}")
print(f"Max : {list_grade[max_grade]}")
print(f"Min : {list_grade[min_grade]}")