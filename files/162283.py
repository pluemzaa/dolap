label = []
data = []
while True :
    vec = input("Enter data example (x1,x2,x3 ...): ")
    if vec == "exit" :
        break
    else :
        vec = vec.split(',')
        vec = [float(i) for i in vec]
        data.append(vec)

        lab = input("Enter data example (y): ")
        label.append(lab)

pred = input("Prediction, enter your input (x1,x2,x3 ...):")
pred = pred.split(',')
pred = [float(i) for i in pred]

mindiff = float('inf')
minindex = -1
for i in range(len(data)) :
    ud = 0
    for j in range(len(data[i])) :
        ud += abs(data[i][j] - pred[j])**2
    ud = ud ** 0.5

    if ud < mindiff :
        mindiff = ud
        minindex = i
print(f"Min Euclidean distance: {mindiff : .2f}")
print(f"Result : {label[minindex]}")