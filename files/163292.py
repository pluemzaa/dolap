print("===== Calculate Grade Program =====")

students = []
grades = []

count = 1
while True:
    name = input(f"Enter student name No.{count} : ").strip()
    grade = float(input("Enter Grade : "))
    students.append(name)
    grades.append(grade)
    
    cont = input("Continue? (y/n) : ").strip().lower()
    if cont == "n":
        break
    count += 1

avg = sum(grades) / len(grades)

max_index = grades.index(max(grades))
min_index = grades.index(min(grades))

print("\n===== Report =====")
print(f"Average : {avg:.2f}")
print(f"Max : {students[max_index]}")
print(f"Min : {students[min_index]}")