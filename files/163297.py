# สร้างโปรแกรมสำหรับเก็บคะแนนนักศึกษา 
# โดยจะรับชื่อ และ เกรดที่นักศึกษา(ควรได้) 
# เสร็จแล้วคิดค่าเฉลี่ยรวม คะแนนมากที่สุด 
# คะแนนน้อยที่สุด เป็นรายงานสรุปผล
# ===== Calculate Grade Program =====
# Enter student name No.1 : Ake
# Enter Grade : 4.00
# Continue? (y/n) : y
# Enter student name No.2 : Boy
# Enter Grade : 3.50
# Continue? (y/n) : y
# Enter student name No.3 : Joey
# Enter Grade : 3.00
# Continue? (y/n) : n

print("===== Calculate Grade Program =====")
number = 1
max_gpx = 0.00
min_gpx = 4.00
max_name = None
min_name = None
total_gpx = 0
while True:
    name = input(f"Enter student name No.{number} : ")
    gpx = float(input("Enter Grade : "))
    
    if gpx > max_gpx:
        max_gpx = gpx
        max_name = name
    if gpx < min_gpx:
        min_gpx = gpx
        min_name = name

    total_gpx += gpx
    con = input("Continue? (y/n) : ")
    
    if con == 'n':
        break
    number += 1
print()
print("===== Report =====")
print(f"Average : {(total_gpx/number):.2f}")
print(f"Max : {max_name}")
print(f"Min : {min_name}")