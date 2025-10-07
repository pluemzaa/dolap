print("===== Calculate Grade Program =====")

n = None
i = 0
h = {}
while n != "n":
    s = input(f"Enter student name No.{i+1} : ")
    g = float(input("Enter Grade : "))
    n = input("Continue? (y/n) : ")
    h[g] = s
    i += 1
    

a = sum(h.keys())/len(h.keys())
mi = min(h.keys())
ma = max(h.keys())
print()
print("===== Report =====")
print(f"Average : {a:.2f}")
print(f"Max : {h[ma]}")
print(f"Min : {h[mi]}")