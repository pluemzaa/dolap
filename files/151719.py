# สร้าง dictionary สำหรับรหัสสัตว์
code = {
    "Dog": 0,
    "Cat": 1,
    "Fish": 2
}

# รับอินพุตจากผู้ใช้
text = input("Enter your pets: ") # เช่น Dog,Cat,Dog,Fish,Cat

# แยก string เป็น list
pets = text.split(",")

# แปลงชื่อสัตว์เป็นรหัส แล้วเก็บลง list
result = []
for i in pets:
    result.append(str(code[i]))

  
# แสดงผลตาม format ที่โจทย์ต้องการ
print("Code of your pets:", ",".join(result))