i = 0
sum = 0
a = float(input("Enter a number (enter 0 to stop):"))
while a != 0 :
    if a != 0:    
        a = float(input("Enter a number (enter 0 to stop):"))
        sum += a 
        i += 1
        print (f'Average:{sum/i :.1f}')
    else:
        print("No numbers entered.")