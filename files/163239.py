print("===== Calculate Grade Program =====")
students = []
grades = []
i = 1
while True:
    name = input(f"Enter student name No.{i} : ")
    grade = float(input("Enter Grade : "))
    students.append(name)
    grades.append(grade)
    cont = input("Continue? (y/n) : ")
    if cont != 'y':
        break
    i += 1

print("\n===== Report =====")
average = sum(grades) / len(grades)
max_index = grades.index(max(grades))
min_index = grades.index(min(grades))
print(f"Average : {average:.2f}")
print(f"Max : {students[max_index]}")
print(f"Min : {students[min_index]}")