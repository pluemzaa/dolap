x ={}
x_list = []
for i in range(4):
    print("Enter item",i+1,end=(''))
    y = input(" : ")
    x_list.append(y)
    print("Enter weight",i+1,end=(''))
    weight = float(input(" : "))
    x[y] = weight

num = 0
for i in range(len(x)):
    print(x_list[i],"%.2f" %x[x_list[i]])
    num += x[x_list[i]]

print('--------------------------- ')
print('total', "%.2f" %num)