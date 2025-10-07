print("===== Calculate Grade Program =====")

total = 0
count = 0

max_score = None
max_name = ""
min_score = None
min_name = ""

number = 1

while True:
    name = input("Enter student name No.%d : " % number)
    grade = float(input("Enter Grade : "))

    total = total + grade
    count = count + 1

    if max_score is None or grade > max_score:
        max_score = grade
        max_name = name

    if min_score is None or grade < min_score:
        min_score = grade
        min_name = name

    cont = input("Continue? (y/n) : ")
    if cont == "n":
        break

    number = number + 1

print("")  # บรรทัดว่าง
print("===== Report =====")
print("Average : %.2f" % (total / count))
print("Max : " + max_name)
print("Min : " + min_name)