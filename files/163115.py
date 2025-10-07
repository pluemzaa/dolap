students = []
student_count = 1

print("===== Calculate Grade Program =====")

while True:
    name = input(f"Enter student name No.{student_count} : ")
    grade = float(input("Enter Grade : "))

    student_data = {"name": name, "grade": grade}
    students.append(student_data)

    student_count += 1

    continue_choice = input("Continue? (y/n) : ").lower() 
    if continue_choice != 'y':
        break 


if not students:
    print("\nNo student data entered. Exiting.")
else:
    all_grades = [student['grade'] for student in students]
    average_grade = sum(all_grades) / len(students)

    max_student = max(students, key=lambda student: student['grade'])

    min_student = min(students, key=lambda student: student['grade'])

    print("\n===== Report =====")
    print(f"Average : {average_grade:.2f}")
    print(f"Max : {max_student['name']}")
    print(f"Min : {min_student['name']}")