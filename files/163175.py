item = {}
item_index = []
for i in range(4):
    print("Enter item",i+1,end=(''))
    I_item = input(" : ")
    item_index.append(I_item)
    print("Enter weight",i+1,end=(''))
    I_weight = float(input(" : "))
    item[I_item] = I_weight
    
sum = 0
for i in range(len(item)):
    print(item_index[i],"%.2f" %item[item_index[i]])
    sum += item[item_index[i]]
    
print("---------------------------")
print("total", "%.2f" %sum)