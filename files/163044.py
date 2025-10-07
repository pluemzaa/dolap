students = []
total_grade = 0.0

count = 0

print("===== Calculate Grade Program =====")

while True:
    count += 1
    name = input(f"Enter student name No.{count} : ")
    grade = float(input("Enter Grade : "))
    
    students.append((name, grade))
    
    total_grade += grade
    
    continue_program = input("Continue? (y/n) : ").lower()
    if continue_program == 'n':
        break

average_grade = total_grade / count

max_grade_student = max(students, key=lambda item: item[1])
min_grade_student = min(students, key=lambda item: item[1])

print("\n===== Report =====")
print(f"Average : {average_grade:.2f}")
print(f"Max : {max_grade_student[0]}")
print(f"Min : {min_grade_student[0]}")