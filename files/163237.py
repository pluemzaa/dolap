m = int(input(" "))
k = int(input(" "))
n = int(input(" "))
c = (m*k)
cal = c/n

if c%n != 0:
     cal+=1
print(int(cal))