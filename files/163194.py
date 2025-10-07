i = 0
total = 0
f = []
w = []
while i < 4:
    m = input(f"Enter item {i+1} : ")
    n = float(input(f"Enter weight {i+1} : "))
    f.append(m)
    w.append(n)
    total += n
    i += 1
    
    
for a, b in zip(f, w):
    print(f"{a}          {b:.2f}")
print("---------------------------")
print(f"total           {total:.2f}")