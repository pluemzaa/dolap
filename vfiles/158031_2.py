i = 0
sum = 0
a = float(input("enter"))
while a != 0 :
    a = float(input("enter"))
    sum += a 
    i += 1
if a != 0:
    print (f'Average:{sum/i :.1f}')
else:
    print("No numbers entered")