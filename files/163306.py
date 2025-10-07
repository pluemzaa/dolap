students = []
grades = []

while True:
    name = input(f"Enter student name No.{len(students) + 1} : ")
    grade = float(input("Enter Grade : "))
    students.append((name, grade))
    grades.append(grade)
    
    if input("Continue? (y/n) : ") != 'y':
        break

average = sum(grades) / len(grades)
max_grade = max(students, key=lambda x: x[1])
min_grade = min(students, key=lambda x: x[1])

print("\n===== Report =====")
print(f"Average : {average:.2f}")
print(f"Max : {max_grade[0]}")
print(f"Min : {min_grade[0]}")