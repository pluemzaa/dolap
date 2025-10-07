total = 0
c=1
number =int(input("Enter a number(enter 0 to stop):"))
while number !=0:
    total=total+number
    c=c+1
    number =int(input("Enter a number(enter 0 to stop):"))
if c >0 :
    Average=total/c
    print("Average: ",Average)
else :
    print("No numbers entered.")