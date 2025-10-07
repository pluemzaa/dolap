print("===== Calculate Grade Program =====")

students = []
grades = []

cont = 1

while True:
    name = input(f"Enter student name No.{cont} : ")
    Grade = float(input('Enter Grade : '))

    students.append(name)
    grades.append(grade)
    
    cont = input("Continue? (y/n) : ").strip().lower()
    if cont == 'n':
        break

    count += 1

average = sum(grades) / len(grades)


max_grade_index = grades.index(max(grades))
min_grade_index = grades.index(min(grades))

print("\n===== Report =====")
print(f"Average : {average:.2f}")
print(f"max : {students[max_grade_index]}")
print(f"min : {students[min_grade_index]}")