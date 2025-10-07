data = []
label = []

while True:
    X = input("Enter data example (x1,x2,x3 ...): ")
    if X == "exit":
        break 
    X = X.split(',')
    X = [int(i) for i in X]
    data.append(X)

    Y = input("Enter data example (y): ")
    label.append(Y)

X_in = input("Prediction, enter your input (x1,x2,x3 ...): ")
X_in = X_in.split(",")
X_in = [int(i) for i in X_in]
p2 = []
if len(X_in) == len(data[0]):
    for i in range(len(data)):
        p = []
        for j in range(len(X_in)): 
            z = (X_in[j]-data[i][j])**2
            p.append(z)
        p2.append(p)

    q = []
    for i in range(len(p2)): 
        a = 0
        for j in range(len(p2[i])):
            a += p2[i][j]   
        a = a**(1/2)
        q.append(a)
    min_ = float("inf")
    min_i = -1
    for c in range(len(q)):
        if q[c] < min_:
            min_ = q[c]
            min_i = c

    print(f"Min Euclidean distance: {min_:.2f}")
    print(f"Result: {label[min_i]}")

else:
    print("Error: Vectors must have the same size")