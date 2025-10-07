fruit_append= []
wegiht_append = []

for i in range(1,5,1):
    fruit = str(input(f"Enter item {i} :"))
    fruit_append.append(fruit)
    
    wegiht = float(input(f"Enter weight {i}:"))
    wegiht_append.append(wegiht)
    
# for i in fruit_append[0]:    
for i in range(len(fruit_append)):
    print(fruit_append[i],end=""),print("           ",end=""),print(wegiht_append[i])
    
    
print("--------------------------- ")
total = sum(wegiht_append)
total = float(total)
print(f"total           {total:.2f}")