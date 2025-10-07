student_list = []
grade_list = []
count = 1
print("===== Calculate Grade Program =====")
while True :
    student = input(f"Enter student name No.{count} : ")
    grade = float(input("Enter Grade : "))
    cont = input("Continue? (y/n) : ")
    student_list.append(student)
    grade_list.append(grade)
    count += 1
    if cont == "y" :
        continue
    else :
        break
minx = min(grade_list)
maxx = max(grade_list)
for i in range(len(grade_list)):
    if grade_list[i] == min(grade_list):
        minx = grade_list[i]
        index_min = i
    if grade_list[i] == max(grade_list):
        maxx = grade_list[i]
        index_max = i
avg = sum(grade_list) / len(grade_list)
print ("===== Report =====")
print(f"Average : {avg:.2f}")
print(f"Max : {student_list[index_max]}")
print(f"Min : {student_list[index_min]}")