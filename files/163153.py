print("===== Calculate Grade Program =====")

students = []
grades = []

count = 1
while True:
    name = input(f"Enter student name No.{count} : ")
    grade = float(input("Enter Grade : "))

    students.append(name)
    grades.append(grade)

    cont = input("Continue? (y/n) : ")
    if cont != 'y':
        break
    count += 1

av = sum(grades) / len(grades)


max_in = grades.index(max(grades))
min_in = grades.index(min(grades))

print("\n===== Report =====")
print(f"Average : {av:.2f}")
print(f"Max : {students[max_in]}")
print(f"Min : {students[min_in]}")