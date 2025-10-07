try:
    n = int(input("Enter number: "))

    # 2. ตรวจสอบว่าค่า n น้อยกว่า 1 หรือไม่
    if n < 1:
        print("Error number must be 1 or greater")
    else:
        # 3. เริ่มสร้างตารางด้วย while loop
        
        # --- ลูปนอก (Outer Loop) สำหรับควบคุม "แถว" ---
        i = 1  # 1. Initialization: กำหนดตัวแปรแถวเริ่มต้นที่ 1
        while i <= n:  # 2. Condition: ทำงานตราบใดที่แถวปัจจุบัน (i) ยังไม่เกิน n
            
            # กำหนดค่าเริ่มต้นสำหรับแต่ละแถว
            current_num = i
            
            # --- ลูปใน (Inner Loop) สำหรับควบคุม "หลัก" ---
            j = 0  # 1. Initialization: กำหนดตัวแปรหลักเริ่มต้นที่ 0 (จะนับ 0 ถึง n-1)
            while j < n:  # 2. Condition: ทำงานตราบใดที่หลักปัจจุบัน (j) ยังน้อยกว่า n
                
                # คำนวณตัวเลขที่จะแสดงผล (วนกลับมาที่ 1 เมื่อเกิน 9)
                display_num = (current_num - 1) % 9 + 1
                
                # แสดงผลตัวเลขตามด้วยเว้นวรรค
                print(display_num, end=" ")
                
                # เพิ่มค่าเพื่อใช้ในหลักถัดไป
                current_num += 1
                
                j += 1  # 3. Increment: เพิ่มค่าตัวแปรหลักขึ้น 1 เพื่อไปหลักถัดไป
            
            # ขึ้นบรรทัดใหม่เมื่อจบแถว
            print()
            
            i += 1  # 3. Increment: เพิ่มค่าตัวแปรแถวขึ้น 1 เพื่อไปแถวถัดไป

except ValueError:
    # กรณีผู้ใช้ป้อนค่าที่ไม่ใช่ตัวเลข
    print("Invalid input. Please enter an integer.")