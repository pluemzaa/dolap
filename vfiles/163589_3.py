print("===== Calculate Grade Program =====")
d = ''
y1 = []
y2 = []
ui = 0
di = 0
total = 0
t = 1
p = 0
alltotal = 0
dis = -1
lol = 0
mkog = 0
while True:
    l = input(f"Enter student name No.{t} : ")
    g = float(input("Enter Grade : "))
    d = input("Continue? (y/n) : ")
    total = g
    alltotal += total
    y1.append(l)
    y2.append(g)
    if d == 'n':
        break
    t += 1
    p += 1
    if g > dis:
        dis = g
        makog = p
    elif g < dis:
        lol = g
        mkog = p
got = alltotal / len(y1)

print("                ")
print("===== Report =====")
print(f"Average : {got}")
print(f"Max : {y1[makog]}")
print(f"Min : {y1[mkog]}")