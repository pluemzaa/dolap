num = input('Enter a series of numbers separated by commas: ')
num = num.split(",")

for i in range(0,len(num)):
    num[i] = int(num[i])

minx = min(num)
maxx = max(num)
        
print('Normalized values:')  
for i in range(0,len(num)):
    cal = (num[i]-minx)/(maxx-minx)
    print("%.2f" % cal)