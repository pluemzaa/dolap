name = []
grade = []
n = 1
print("===== Calculate Grade Program =====")
while True:
    a = input(f"Enter student name No.{n} : ")
    name.append(a)
    b = float(input("Enter Grade : "))
    grade.append(b)
    c = input("Continue? (y/n) : ")
    n = n+1
    if c == "y":
        continue
    else:
        break
avg = sum(grade)/len(grade)
max_n = grade.index(max(grade))
min_n = grade.index(min(grade))
print()
print("===== Report =====")
print(f"Average : {avg:.2f}")
print("Max :",name[max_n])
print("Min :",name[min_n])