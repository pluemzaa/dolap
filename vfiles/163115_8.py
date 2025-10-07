students = []
student_count = 1

print("===== Calculate Grade Program =====")

# วนลูปเพื่อรับข้อมูลไปเรื่อยๆ จนกว่าผู้ใช้จะตอบ n
while True:
    # รับชื่อและเกรด
    name = input(f"Enter student name No.{student_count} : ")
    
    # ใช้ try-except เพื่อป้องกันกรณีผู้ใช้ใส่ข้อมูลที่ไม่ใช่ตัวเลข
    try:
        grade = float(input("Enter Grade : "))
    except ValueError:
        print("Invalid grade format. Please enter a number.")
        continue # กลับไปเริ่มลูปใหม่โดยไม่เพิ่ม student_count

    # เก็บข้อมูลเป็น dictionary แล้วเพิ่มลงใน list
    student_data = {"name": name, "grade": grade}
    students.append(student_data)
    
    # เพิ่มจำนวนนักศึกษาสำหรับแสดงผลครั้งถัดไป
    student_count += 1

    # ถามว่าจะทำต่อหรือไม่
    continue_choice = input("Continue? (y/n) : ").lower() # .lower() เพื่อให้รองรับทั้ง y และ Y
    if continue_choice != 'y':
        break # ออกจากลูป

# ตรวจสอบว่ามีข้อมูลนักศึกษาหรือไม่ ก่อนทำการคำนวณ
if not students:
    print("\nNo student data entered. Exiting.")
else:
    # --- เริ่มส่วนการคำนวณ ---

    # 1. คำนวณเกรดเฉลี่ย
    # ดึงเกรดของทุกคนออกมาจาก list of dictionaries
    all_grades = [student['grade'] for student in students]
    average_grade = sum(all_grades) / len(students)

    # 2. หาคนที่มีคะแนนสูงสุด
    # ใช้ฟังก์ชัน max() โดยกำหนด key ให้เปรียบเทียบจากค่า 'grade' ใน dictionary
    max_student = max(students, key=lambda student: student['grade'])
    
    # 3. หาคนที่มีคะแนนน้อยที่สุด
    # ใช้ฟังก์ชัน min() โดยกำหนด key ให้เปรียบเทียบจากค่า 'grade' ใน dictionary
    min_student = min(students, key=lambda student: student['grade'])

    # --- เริ่มส่วนการแสดงผลรายงาน ---
    print("\n===== Report =====")
    print(f"Average : {average_grade:.2f}") # .2f เพื่อให้แสดงผลทศนิยม 2 ตำแหน่งเสมอ
    print(f"Max : {max_student['name']}")
    print(f"Min : {min_student['name']}")