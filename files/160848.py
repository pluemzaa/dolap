n = 1
total = 0
check = 0
while n != 0 :
    n = int(input("Enter a number (enter 0 to stop):"))
    if n != 0 :
        total = total + n
        check = check + 1
if check == 0 :
    print ("No numbers entered.")
else :
    avg = total / check
    print ("Average" , avg)