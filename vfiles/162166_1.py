import math

data = []
lab = []
while True:
    num = input("Enter data example (x1,x2,x3 ...): ")
    if num == "exit":
        break
    num = num.split(",")
    for i in range(len(num)):
        num[i] = int(num[i])
    data.append(num)
    kum = input("Enter data example (y): ")
    kum = kum.split(",")
    lab.append(kum)

gum = input("Prediction, enter your input (x1,x2,x3 ...): ")
gum = gum.split(",")
result = 0
min_diff = float('inf')
min_index = -1
total = 0
for u in range(len(gum)):
    gum[u] = int(gum[u])
for i in range (len(lab)):
    d = data[i]
    result = 0
    for i in range (len(d)):
        result = (gum[i] - d[i])**2
        total += result
    pototal = math.sqrt(total)
    if pototal < min_diff:
        min_diff = pototal
        min_index = i

print(f"Min Euclidean distance: {min_diff:.2f}")
print(f"Result : {lab[min_index][0]}")