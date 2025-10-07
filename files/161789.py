num = []
label = []
while True:
    x = input("Enter data example (x1,x2,x3 ...): ").lower()
    if x  == "exit":
        break
    x = x.split(',')
    y = input("Enter data example (y): ")
    x = [int(i) for i in x]
    num.append(x)
    label.append(y)
f = input("Prediction, enter your input (x1,x2,x3 ...): ").split(',')
f = [int(i) for i in f]
s= 0
minl = float('inf')
ind = -1
for i in range(len(num)):
    s=0
    for j in range(len(num[i])):
        s+= ((num[i][j]-f[j])**2)
    s=s**0.5
    if s < minl :
        minl = abs(s)
        ind = label[i]
print(f'Min Euclidean distance: {minl:.2f}')
print(f"Result : {ind}")