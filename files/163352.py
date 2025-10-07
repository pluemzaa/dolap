#===== Calculate Grade Program =====
#Enter student name No.1 : Ake
#Enter Grade : 4.00
#Continue? (y/n) : y
#Enter student name No.2 : Boy
#Enter Grade : 3.50
#Continue? (y/n) : y
#Enter student name No.3 : Joey
#Enter Grade : 3.00
#Continue? (y/n) : n
i = 1
name_list = []

print ("===== Calculate Grade Program =====")

while True :
    name = input(f"Enter student name No.{i} : ")
    grade = float(input("Enter Grade : "))
    name_list.append({'name':name,'grade':grade})

    i += 1
    cont = input("Continue? (y/n) :")
    if cont == "n":
        break

total_grade = 0
max_grade = -1
min_grade = 5
max_name = ""
min_name = ""

for student in name_list :
    total_grade += student['grade']

    if student['grade'] > max_grade :
        max_grade = student['grade']
        max_name = student['name']

    if student['grade'] < min_grade :
        min_grade = student['grade']
        min_name = student['name']

average_grade = total_grade / len(name_list)

print()
print('===== Report =====')
print(f'Average : {average_grade:.2f}')
print(f'Max : {max_name}')
print(f'Min : {min_name}')