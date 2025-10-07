# รับรหัสผ่านจากผู้ใช้
password = input()

# ตรวจสอบความยาวของรหัสผ่าน
if len(password) >= 8:
    print("Password is strong")
else:
    print("Password is weak")