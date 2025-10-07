count = 1
t = 0.0
max_g = min_g = 0.0
max_n = min_n = ""

while True:
    name = input(f"Enter student name No.{count} : ")
    grade = float(input("Enter Grade : "))

    if count == 1:
        max_g = min_g = grade
        max_n = min_n = name
    else:
        if grade > max_g:
            max_g = grade
            max_n = name
        if grade < min_g:
            min_g = grade
            min_n = name

    t += grade
    cont = input("Continue? (y/n) : ")
    if cont != 'y':
        break
    count += 1

avg = t / count

print()
print("----- Report -----")
print(f"Average : {avg:.2f}")
print(f"Max : {max_n}")
print(f"Min : {min_n}")