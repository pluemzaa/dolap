print("===== Calculate Grade Program =====")
x = 1
gt = 0
ns = 0
lgt = []
lns = []
while True:
    n = input(f"Enter student name No.{x}: ")
    x += 1
    ns += 1
    lns.append(n)
    g = float(input(f"Enter Grade: "))
    gt += g
    lgt.append(g)
    c = input("Continue? (y/n) : ")
    if c == "n":
        break
    elif c == "y":
        continue

print("\n===== Report =====")
print(f"Average : {gt/ns:.2f}")
Max = lgt[0]
Min = lgt[0]
index_max = lgt.index(max(lgt))
index_min = lgt.index(min(lgt))
print(f"Max : {lns[index_max]}")
print(f"Min : {lns[index_min]}")