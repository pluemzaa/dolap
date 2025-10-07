# รับค่า key จากผู้ใช้
key = int(input("Enter key"))

# ข้อความที่จะเข้ารหัส
text = "hello"
result = ""

# เข้ารหัสแต่ละตัวอักษร
for char in text:
    # แปลงตัวอักษรเป็นรหัส ASCII
    ascii_code = ord(char)
    # คำนวณรหัสใหม่ (เฉพาะ a-z)
    new_code = (ascii_code - 97 + key) % 26 + 97
    # แปลงกลับเป็นตัวอักษร
    result += chr(new_code)

# แสดงผลลัพธ์
print(f"Cipher of {text} is {result}")