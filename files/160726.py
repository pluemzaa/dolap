num = input("Enter a series of numbers separated by commas: ")
num = num.split(",")

for i in range (0,len(num)) :
    num[i] = int(num[i])

_max = num[0]
for i in range (0,len(num)) :
    if num[i] > _max :
        _max = num[i]

_min = num[0]
for i in range (0,len(num)) :
    if num[i] < _min :
        _min = num[i]

print ("Normalized values:")

for i in range (0,len(num)) :
    num_cal = ((num[i]-_min)/(_max-_min))
    print ("%.2f"%num_cal)