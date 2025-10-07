#จงเขียนโปรแกรมเครื่องคิดเลขอัฉริยะ
#โดยรับตัวเลข 2 จำนวน และตัวดำเนินการ ทางแป้นพิมพ์
#โดยจะโปรแกรมจะตรวจสอบตามสัญลักษณ์ที่ผู้ใช้ป้อน เช่น '+' ให้นำตัวเลขมาบวกกัน
#และโปรแกรมจะมีการตรวจสอบเพิ่มเติม ดังนี้
#1. กรณีที่ผู้ใช้งานป้อนตัวดำเนินการ อื่นๆ นอกจาก +, -, *, / จะแสดงข้อความ
# Invalid operator
#2. กรณีการหาร ต้องตรวจสอบตัวหารว่าเป็น 0 หรือไม่ หากเป็น 0 จะแสดงข้อความ
# Cannot divide by zero
#ตัวอย่างหน้าจอ #1
#Enter the first number: 10
#Enter the second number: 30
#Enter the operator (+, -, *, /): *
#Result : 300.00

f = int(input("Enter the first number: "))
s = int(input("Enter the second number: "))
op = str(input("Enter the operator (+, -, *, /): "))
a = 0
if s<=0 and op is "/":
    print("Cannot divide by zero")
else:
    if op == "+":
        a = f+s
        print(f"Result :{a:.2f}")
    elif op == "-":
        a = f-s
        print(f"Result :{a:.2f}")
    elif op == "*":
        a = f*s
        print(f"Result :{a:.2f}")
    elif op == "/":
        a = f/s
        print(f"Result :{a:.2f}")
    else:
        print("Invalid operator")