print("===== Calculate Grade Program =====")
count=1
total = 0.0
max_grade = 0.0
min_grade = 0.0
max_name = ""
min_name = ""

while True:
    name = input(f"Enter student name No.{count} : ")
    grade = float(input("Enter Grade : "))
        
    if count == 1:
        max_grade = min_grade = grade
        max_name = min_name = name
    else:
        if grade > max_grade:
            max_grade = grade
            max_name = name
        if grade < min_grade:
            min_grade = grade
            min_name = name
        
    total += grade
    cont = input("Continue? (y/n) : ")
    if cont != 'y':
        break
    count += 1

avg = total / count

print()
print("===== Report =====")
print(f"Average : {avg:.2f}")
print(f"Max     : {max_name}")
print(f"Min     : {min_name}")