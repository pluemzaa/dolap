'''จงเขียนโปรแกรมเพื่อค้นหาตัวเลขใหลิสต์โดยทำงานดังนี้

รับค่าตัวเลขจำนวนเต็มหลายค่าจากผู้ใช้ โดยให้คั่นค่าด้วยเครื่องหมายจุลภาค (,)
รับค่าจำนวนเต็มอีก 1 ค่า จากผู้ใช้ เพื่อใช้เป็นค่าที่ต้องการค้นหา
ตรวจสอบว่าค่าที่ต้องการค้นหานั้นปรากฏอยู่ในรายการหรือไม่
หากพบ ให้แสดงข้อความในรูปแบบ
Found <ค่าที่ค้นหา> at index <ตำแหน่ง>
โดยแสดงทุกๆตำแหน่งที่พบ
หากไม่พบ ให้แสดงข้อความในรูปแบบ
No <ค่าที่ค้นหา> found

Enter numbers separated by commas: 10,20,30,10
Enter number to search: 10
Found 10 at index 0
Found 10 at index 3

Enter numbers separated by commas: 1,2,3
Enter number to search: 10
No 10 found.

'''

text = list(map(lambda x:int(x) ,input("Enter numbers separated by commas: ").split(',')))
search_num = int(input("Enter number to search: "))

ever_found = False
for i,num in enumerate(text):
    if num == search_num:
        ever_found = True
        print(f"Found {search_num} at index {i}")

if not ever_found:
    print(f"No {search_num} found.")