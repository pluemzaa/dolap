# รับข้อมูลจากผู้ใช้
name = input("Enter your name: ")
email = input("Enter your email: ")
gpa = float(input("Enter your GPA: "))

# เก็บข้อมูลในรูปแบบ List
data_list = [name, email, gpa]

# เก็บข้อมูลในรูปแบบ Tuple
data_tuple = (name, email, gpa)

# เก็บข้อมูลในรูปแบบ Dictionary
data_dict = {
    'name': name,
    'email': email,
    'GPA': gpa
}

# แสดงผลลัพธ์
print(data_list)
print(data_tuple)
print(data_dict)