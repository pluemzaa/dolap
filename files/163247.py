print("===== Calculate Grade Program =====")

students = []
grades = []

count = 1

while True:
    name = input(f"Enter student name No.{count} : ")
    grade = float(input("Enter Grade : "))
    students.append(name)
    grades.append(grade)

    cont = input("Continue? (y/n) : ").lower()
    if cont != 'y':
        break
    count += 1

print("\n" + " " * 20)  

print("===== Report =====")

average = sum(grades) / len(grades)


max_grade = max(grades)
min_grade = min(grades)

max_index = grades.index(max_grade)
min_index = grades.index(min_grade)

print(f"Average : {average:.2f}")
print(f"Max : {students[max_index]}")
print(f"Min : {students[min_index]}")