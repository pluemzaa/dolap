print("===== Calculate Grade Program =====")
student = []
Grade = []
n = 1
while True:
    name = input(f"Enter student name No.{n} : ")
    grade = float(input("Enter Grade : "))
    student.append(name)
    Grade.append(grade)
    x = input("Continue? (y/n) : ")
    if x == "n":
        break
    n += 1

average = sum(Grade) / len(Grade)
max = Grade.index(max(Grade))
min = Grade.index(min(Grade))
print()
print("===== Report =====")
print(f"Average : {average:.2f}")
print(f"Max : {student[max]}")
print(f"Min : {student[min]}")