fruit_append= []
wegiht_append = []

for i in range(1,5,1):
    fruit = str(input(f"Enter item {i} : "))
    fruit_append.append(fruit)
    
    wegiht = float(input(f"Enter weight {i}: "))
    
    wegiht_append.append(wegiht)
    
# for i in range(len(wegiht_append)):
#     wegiht(i) = f"{wegiht(i):.2f}"
    
for i in range(len(fruit_append)):  
    print(fruit_append[i],end=""),print("           ",end=""),print(f"{wegiht_append[i]:.2f}")
    
    
print("---------------------------")
total = sum(wegiht_append)
total = float(total)
print(f"total           {total:.2f}")