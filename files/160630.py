num =input("Enter a series of numbers separated by commas:")
num = num.split(",")
n = len(num)

for i in range(len(num)):
    num[i] = int(num[i])
    
_max = max(num)
_min = min(num)
print ("Normalized values:")
for i in range(n):
    s = (num[i]-_min)/(_max - _min)
    print ("%.2f"%s)