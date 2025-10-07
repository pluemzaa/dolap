#2
x = input("Enter a series of numbers separated by commas:").split(",")
for i in range (len(x)) :
    x[i] = int(x[i])
mac = x[0]
for j in range(len(x)) : 
    if x[j] > mac :
        mac = x[j]
        print (f"set the maximum value to {x[j]}")
print (f"The maximum value is {mac}")