ให้นักศึกษาเขียนโปรแกรมคำนวนค่า Euclidean distance ของเวกเตอร์สองเวอเตอร์

สูตรทั่วไปของ Euclidean distance เขียนได้ตามรูปด้านล่าง โดยที่ q คือ vector1 และ p คือ vector2 และความยาวของทั้งสองเวคเตอร์เท่ากับ n


 

ตัวอย่างเช่น q = (30, 50, 60, 100), p = (20, 75, 50, 45)

d = Sqrt( (30-20)**2 + (50-75)**2 +(60-50)**2 + (100-45)**2 )


โปรแกรมจะวนซ้ำเพื่อหาผลต่างกำลังสองก่อนแล้วจึงหารากที่สอง

และให้ตรวจตรวจสอบหากผู้ใช้ป้อนเวกเตอร์ขนาดไม่เท่ากัน ให้แสดงข้อความแจ้งเตือน

ตัวอย่างผลลัพธ์ #1:

Enter coordinates of point P (p1, p2,...,qn): 1,2,3
Enter coordinates of point Q (q1, q2,..., qn): 4,5,6
Euclidean distance between point P and point Q: 5.20
ตัวอย่างผลลัพธ์ #2:

Enter coordinates of point P (p1, p2,...,qn): 1,2,3,4,5
Enter coordinates of point Q (q1, q2,..., qn): 1,2,3,4,5
Euclidean distance between point P and point Q: 0.00
ตัวอย่างผลลัพธ์ #3: กรณีป้อนเวกเตอร์ขนาดไม่เท่ากัน

Enter coordinates of point P (p1, p2,...,qn): 1,2,3
Enter coordinates of point Q (q1, q2,..., qn): 1,2
Error: Vectors must have the same size