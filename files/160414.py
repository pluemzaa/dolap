en = (input("Enter a series of numbers separated by commas: "))
en = en.split(",")
i = 0
 
for i in range(0,len(en)):
    en[i] = int(en[i])
maxn = en[0]
for i in range(0,len(en)):
    if en[i] > maxn:
        maxn = en[i] 
        print('set the maximum value to',maxn) 
print('The maximum value is',maxn)