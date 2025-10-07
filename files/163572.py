print("===== Calculate Grade Program =====")

students = []  # เ


count = 1
while True:
    name = input(f"Enter student name No.{count} : ").strip()
    grade = float(input("Enter Grade : "))
    students.append((name, grade))

    cont = input("Continue? (y/n) : ").strip().lower()
    if cont != "y":
        break
    count += 1

print("                ") 
print("===== Report =====")


grades = [g for _, g in students]
average = sum(grades) / len(grades)


max_student = max(students, key=lambda x: x[1])[0]
min_student = min(students, key=lambda x: x[1])[0]

print(f"Average : {average:.2f}")
print(f"Max : {max_student}")
print(f"Min : {min_student}")