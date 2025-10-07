x ={}
x_index = []
for i in range(4):
    print("Enter item",i+1,end=(''))
    y = input(" : ")
    x_index.append(y)
    print("Enter weight",i+1,end=(''))
    z = float(input(" : "))
    x[y] = z

Sum = 0
for i in range(len(x)):
    print(x_index[i],"%.2f" %x[x_index[i]])
    Sum += x[x_index[i]]

print('--------------------------- ')
print('total', "%.2f" %Sum)