print("===== Calculate Grade Program =====")

students = {}
i = 1
while True:
    name = input(f"Enter student name No.{i} : ")
    grade = float(input("Enter Grade : "))
    students[name] = grade
    if input("Continue? (y/n) : ").lower() != 'y':
        break
    i += 1

print("\n" * 5)
print("===== Report =====")

grades = list(students.values())
avg = sum(grades) / len(grades)
max_name = max(students, key=students.get)
min_name = min(students, key=students.get)

print(f"Average : {avg:.2f}")
print(f"Max : {max_name}")
print(f"Min : {min_name}")