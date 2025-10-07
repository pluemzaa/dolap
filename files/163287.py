print("===== Calculate Grade Program =====")

students = []  
count = 1

while True:
    name = input(f"Enter student name No.{count} : ")
    grade = float(input("Enter Grade : "))
    students.append((name, grade))
    
    cont = input("Continue? (y/n) : ").lower()
    if cont != 'y':
        break
    count += 1

total = sum(grade for _, grade in students)
average = total / len(students)

max_student = max(students, key=lambda x: x[1])[0]
min_student = min(students, key=lambda x: x[1])[0]

print("\n===== Report =====")
print(f"Average : {average:.2f}")
print(f"Max : {max_student}")
print(f"Min : {min_student}")