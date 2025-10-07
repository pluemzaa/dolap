# เขียนโปรแกรมรับชื่อผลไม้ และ น้ำหนักของผลไม้ 
# โดยรับผลไม้ทั้งหมด 4 ชนิด และรับทีละบรรทัด 
# จากนั้นแสดงผลรวมน้ำหนักทั้งหมดในบรรทัดสุดท้าย 
# นำมาแสดงผลดังกรณีทดสอบ

f = input("Enter item 1 : ")
w = float(input("Enter weight 1 : "))
f1 = input("Enter item 2 : ")
w1 = float(input("Enter weight 2 : "))
f2 = input("Enter item 3 : ")
w2 = float(input("Enter weight 3 : "))
f3 = input("Enter item 4 : ")
w3 = float(input("Enter weight 4 : "))
s1 = w+w1+w2+w3

print(f,"       %.2f"%w)
print(f1,"      %.2f"%w1)
print(f2,"      %.2f"%w2)
print(f3,"      %.2f"%w3)
print("---------------------------")
print("total",'%.2f'%s1)