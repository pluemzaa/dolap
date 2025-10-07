print("----- Calculate Grade Program -----")

students = [] grades = []

count = 1

while True:
    name = input(f"Enter student name No.{count} : ")
    grade = float(input("Enter Grade : "))
    students.append(name)
grades.append(grade)

cont = input("Continue? (y/n) : ").strip().lower()
if cont == 'n':
    break

count += 1
print("----- Calculate Grade Program -----")

students = []
grades = []

count = 1

while True:
    name = input(f"Enter student name No.{count} : ")
    grade = float(input("Enter Grade : "))

    students.append(name)
    grades.append(grade)

    cont = input("Continue? (y/n) : ").strip().lower()
    if cont == 'n':
        break

    count += 1

average = sum(grades) / len(grades)

max_grade_index = grades.index(max(grades))
min_grade_index = grades.index(min(grades))

print("===== Report =====")
print(f"Average : {average:.2f}")
print(f"Max : {students[max_grade_index]}")
print(f"Min : {students[min_grade_index]}")