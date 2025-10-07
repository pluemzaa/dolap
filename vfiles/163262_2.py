x = int(input("Enter the number of rows for the pyramid:"))
type_count = "odd"
count = 0
for i in range(1,x+1):
    count += 1*i
if count%2 == 0 :
    type_count = "even"
print(f"The total number of boxes: {count}")
print (f"The total number of boxes is {type_count}")
if count % 2 == 0 :
    for i in range(1,x+1):
        print(f"{i} "*i)
else :
    for i in range(x,0,-1):
        print(f"{i} "*i)