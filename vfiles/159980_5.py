print("1. ต้องมีความยาวมากกว่า 8 ตัวอักษร")
print("2. ต้องประกอบไปด้วยตัวอักษรพิมพ์ใหญ่และพิมพ์เล็กอย่างน้อย 1 ตัวอักษร")
print("3. ต้องประกอบไปด้วยตัวเลขอย่างน้อย 1 ตัว")

password = input("Enter a password: ")
if len(password) >= 8 :
  print("Password is valid.")
else :
  print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")