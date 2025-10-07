print("===== Calculate Grade Program =====")

students = [] 
i = 1

while True:
    name = input(f"Enter student name No.{i} : ")
    grade = float(input("Enter Grade : "))
    students.append((name, grade))
    
    cont = input("Continue? (y/n) : ").lower()
    if cont != 'y':
        break
    i += 1

total = 0
for s in students:
    total += s[1]
avg = total / len(students)

max_name, max_grade = students[0]
min_name, min_grade = students[0]
for s in students:
    if s[1] > max_grade:
        max_name, max_grade = s
    if s[1] < min_grade:
        min_name, min_grade = s

print()
print("===== Report =====")
print(f"Average : {avg:.2f}")
print(f"Max : {max_name}")
print(f"Min : {min_name}")