print("====== Calculate Grade Program ======")

names = []
grades = []
count = 1

while True:
    name = input(f"Enter student name No.{count} : ")
    grade = float(input("Enter Grade : "))
    names.append(name)
    grades.append(grade)

    cont = input("Continue? (y/n) : ").strip().lower()
    if cont != "y":
        break
    count += 1

average = sum(grades) / len(grades)
max_name = names[grades.index(max(grades))]
min_name = names[grades.index(min(grades))]

print()  # บรรทัดว่างก่อนรายงาน
print("====== Report ======")
print(f"Average : {average:.2f}")
print(f"Max : {max_name}")
print(f"Min : {min_name}")