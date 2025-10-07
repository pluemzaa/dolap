names = []
grades = []
i = 1

while True:
    name = input(f"Enter student name No.{i} : ")
    grade = float(input("Enter Grade : "))
    names.append(name)
    grades.append(grade)

    cont = input("Continue? (y/n) : ").strip().lower()
    if cont != 'y':
        break
    i += 1

avg = sum(grades) / len(grades) if grades else 0.0
max_name = names[grades.index(max(grades))]
min_name = names[grades.index(min(grades))]

print()
print("===== Report =====")
print(f"Average : {avg:.2f}")
print(f"Max : {max_name}")
print(f"Min : {min_name}")