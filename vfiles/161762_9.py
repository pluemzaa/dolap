a = []
b = []

while True:
    ai = input("Enter data example (x1,x2,x3 ...): ")
    if ai.lower() == 'exit':
        break
    
    al = [int(x) for x in ai.split(',')]
    bl = input("Enter data example (y): ")
    
    a.append(al)
    b.append(bl)

ci = input("Prediction, enter your input (x1,x2,x3 ...): ")
cl = [int(x) for x in ci.split(',')]

m = -1
d = ""

for i in range(len(a)):
    e = 0
    for j in range(len(a[i])):
        e = e + (a[i][j] - cl[j])**2
    
    f = e**0.5
    
    if m == -1 or f < m:
        m = f
        d = b[i]

print(f"Min Euclidean distance: {m:.2f}")
print(f"Result : {d}")