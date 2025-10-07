'''จงเขียนโปรแกรมเพื่อรับตัวเลขทางหน้าจอ (กี่ตัวก็ได้ ใช้คั่นด้วย , ) 
แล้วคำนวนค่าสูงสุดโดยใช้คำสั่งวนซ้ำหากค่าสูงสุด (maximum) มีการเปลี่ยนแปลง จะแสดงข้อความออกทางจอภาพ 


ตัวเลขตัวแรกของ list จะถูกกำหนดเป็นค่า maximun เริ่มต้น

Enter a series of numbers separated by commas: 0,1,5,5,1,7
set the maximum value to 1
set the maximum value to 5
set the maximum value to 7
The maximum value is 7

Enter a series of numbers separated by commas: 1,10,5,5,4,0,4,8
set the maximum value to 10
The maximum value is 10'''

text = list(map(lambda x:int(x) ,input("Enter a series of numbers separated by commas: ").split(',')))

max = text[0]
for i in text:
    if i > max:
        max = i
        print(f"set the maximum value to {i}")
print(f"The maximum value is {max}")