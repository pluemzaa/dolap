print("===== Calculate Grade Program =====")

students = []  
grades = []    

count = 1
while True:
    name = input(f"Enter student name No.{count} : ")
    grade = float(input("Enter Grade :"))
    
    students.append(name)
    grades.append(grade)
    
    cont = input("Continue? (y/n) : ").lower()
    if cont != 'y':
        break
    count += 1


average = sum(grades) / len(grades)


max_index = grades.index(max(grades))
min_index = grades.index(min(grades))

max_student = students[max_index]
min_student = students[min_index]


print("\n")  
print("===== Report =====")
print(f"Average :{average:.2f}")
print(f"Max :{max_student}")
print(f"Min :{min_student}")