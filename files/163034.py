Items = {}
Items_index = []
for i in range(4):
    print("Enter item",i+1,end=(''))
    I_Item = input(" : ")
    Items_index.append(I_Item)
    print("Enter weight",i+1,end=(''))
    I_Weight = float(input(" : "))
    Items[I_Item] = I_Weight
    
Sum = 0

for i in range(len(Items)):
    print(Items_index[i],"%.2f" %Items[Items_index[i]])
    Sum += Items[Items_index[i]]

print("---------------------------")
print("total", "%.2f" %Sum)