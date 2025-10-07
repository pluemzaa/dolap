CALORIES_PER_STEP = 0.06 # เปลี่ยนชื่อตัวแปรให้สื่อความหมายมากขึ้น

try:
    steps = int(input("Enter the number of steps taken: "))
    if steps < 0:
        print("Number of steps cannot be negative. Please enter a valid number.")
    else:
        calories_burned = steps * CALORIES_PER_STEP # ใช้งานตัวแปรชื่อใหม่
        print("Total calories burned: %.2f calories" % calories_burned)
except ValueError: # เพิ่มการจัดการข้อผิดพลาดสำหรับ input ที่ไม่ใช่ตัวเลข
    print("Invalid input. Please enter a whole number for steps.")