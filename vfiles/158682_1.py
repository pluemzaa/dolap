c = 0
total = 0
i = int(input("Enter a number (enter 0 to stop):"))
while i != 0:
    total = total + i
    i = int(input("Enter a number (enter 0 to stop):"))
    c = c+1
    
a = total/c
print(a)