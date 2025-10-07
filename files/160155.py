#1
x = input("Enter numbers separated by commas: ").split(",")
y = int(input("Enter number to search: "))
c = 0
for i in range (len(x)) :
    x[i] = int(x[i])
for j in range(len(x)):
    if  y == x[j] :
        print (f"Found {y} at index {j}")
        c += 1
if c == 0 :
    print (f"No {y} found.")