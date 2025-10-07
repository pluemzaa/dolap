print("===== Calculate Grade Program =====")

students = []
grades = []
no = 1

while True:
    name = input(f"Enter student name No.{no} : ")
    while True:
            grade = float(input("Enter Grade : "))
            break  
    students.append(name)
    grades.append(grade)
    cont = input("Continue? (y/n) : ")
    if cont == 'n':
        break
    no += 1

print("\n===== Report =====")
avg = sum(grades) / len(grades)
max_index = grades.index(max(grades))
min_index = grades.index(min(grades))

print(f"Average : {avg:.2f}")
print(f"Max : {students[max_index]}")
print(f"Min : {students[min_index]}")