import math

X = []
Y = []

while True:
    x = input("Enter data example (x1,x2,x3 ...): ")
    if x.lower() == "exit":
        break
    lbl = input("Enter data example (y): ")
    X.append([float(i) for i in x.split(",")])
    Y.append(lbl)

px = input("Prediction, enter your input (x1,x2,x3 ...): ")
pv = [float(i) for i in px.split(",")]

md = None
res = None

for i in range(len(X)):
    if len(X[i]) != len(pv):
        print("Error: Vector sizes do not match")
        exit()
    d = math.sqrt(sum((X[i][j] - pv[j]) ** 2 for j in range(len(X[i]))))
    if md is None or d < md:
        md = d
        res = Y[i]

print(f"Min Euclidean distance: {md:.2f}")
print(f"Result : {res}")