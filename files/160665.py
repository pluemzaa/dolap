num = input("Enter a series of numbers separated by commas: ")
num = num.split (",")

for i in range (0,len(num)) :
    num[i] = int(num[i])


min_x = min(num)
max_x = max(num)
_max = num[0]
print ("Normalized values:")
for i in range (0,len(num)) :
    r = (num[i]-min_x)/(max_x-min_x)
    print (f"{r:.2f}")