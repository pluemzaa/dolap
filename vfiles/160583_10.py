x = input("Enter a series of numbers separated by commas: ")
x = x.split(',')

maximum = int(x[0])
showed = False

for i in x[1:]:
    n = int(i)
    if n > maximum:
        maximum = n
        print(f"set the maximum value to {maximum}")
        showed = True
        
# ถ้าไม่มีค่าบรรทัด set ที่ไหนเลย (แปลว่าตัวแรกสุดคือมากสุดอยู่แล้ว)
if not showed:
    print(f"set the maximum value to {maximum}")

print(f"The maximum value is {maximum}")