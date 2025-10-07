print("===== Calculate Grade Program =====")
names = []
grade = []
n = 1
while True:
    name = input(f"Enter student name No.{n} : ")
    names.append(name)
    gr = float(input("Enter Grade : "))
    grade.append(gr)
    con = input("Continue? (y/n) : ")
    n = n+1
    if con == "n":
        break
print("")
print("===== Report =====")
av = 0
_max = 0
_min = 0
gmax = 0
gmin = 0
for i in range(len(grade)):
    av = av + grade[i]
av = av / len(grade)
for i in range(len(grade)):
    if grade[i] > _max:
        _max = grade[i]
        gmax = i
    if grade[i] < _max:
        _min = grade[i]
        gmin = i

print("Average : %.2f"%av)
print("Max : ",names[gmax])
print("Min : ",names[gmin])