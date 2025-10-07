data = []
label = []
while True:
    n = input('Enter data example (x1,x2,x3 ...):')
    if n == 'exit':
        break
    n = n.split(',')
    n = [float(x) for x in n]
    data.append(n)
    
    lab = input('Enter data example (y):')
    label.append(lab)
    
e = input('Prediction, enter your input (x1,x2,x3 ...):').split(',')
e = [float(x) for x in e]

md = float('inf')
mi = -1
for i in range(len(label)):
    v1 = data[i]
    s = 0
    for j in range(len(v1)):
        s += (v1[j] - e[j])**2
    s = s**0.5
    if s < md:
        md = s
        mi = i
print(f'Min Euclidean distance: {md:.2f}')
print(f'Result : {label[mi]}')