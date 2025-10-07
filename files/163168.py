print("===== Calculate Grade Program =====")

students = []
grades = []

count = 1

while True:
    name = input(f"Enter student name No.{count} : ")
    grade = float(input("Enter Grade : "))
    
    students.append(name)
    grades.append(grade)
    
    cont = input("Continue? (y/n) :")
    if cont == 'n':
        break
    
    count += 1

average = sum(grade) / len(grade)


max_grade_index = grades.index(max(grades))
min_grade_index = grades.index(min(grades))

print("\n===== Report =====")
print(f"Average : {average:.2f}")
print(f"Max : {max_grade_index:.2f}")
print(f"Min : {min_grade_index:.2f}")