n=input("Enter a series of numbers separated by commas: ")
n=n.split(",")

for i in range(len(n)):
    n[i]=int(n[i])

n1=n[0]
for i in range(len(n)):
    if n[i] > n1:
        n1 =n[i]
        print("set the maximum value to",n1)
        

print("The maximum value is",n1)