# รับค่า input เป็น string
raw_input = input("Input: ")

# แยกตัวเลขออกจากกันด้วย comma แล้วแปลงเป็น int
a, b = map(int, raw_input.split(','))

# แสดงผลลัพธ์ของแต่ละเครื่องหมาย
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
print(f"{a}//{b}={a//b}")
print(f"{a}%{b}={a%b}")
print(f"{a}**{b}={a**b}")