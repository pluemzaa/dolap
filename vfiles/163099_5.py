z = 1
n = []
g = []
print("===== Calculate Grade Program =====")
while True:
    name = input(f"Enter student name No.{z} : ")
    gpa = float(input("Enter Grade : "))
    con = input("Continue? (y/n) : ")
    n.append(name)
    g.append(gpa)
    if con == 'n':
        break
    z+=1
mx = max(g)
mn = min(g)
for i in range(len(g)):
    if g[i] == mx:
        s = i
    if g[i] == mn:
        l = i
print("===== Report =====")
print(f'Average : {(sum(g)/len(g)):.2f}')
print(f"Max : {n[s]}")
print(f"Min : {n[l]}")