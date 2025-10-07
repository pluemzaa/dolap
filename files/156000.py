# รับค่าตัวเลข 2 ตัวที่คั่นด้วย comma
a, b = map(int, input().split(','))

# คำนวณและแสดงผล
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
print(f"{a}//{b}={a//b}")
print(f"{a}%{b}={a%b}")
print(f"{a}**{b}={a**b}")