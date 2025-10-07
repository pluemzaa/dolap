n=input("Enter numbers: ")
n=n.split(",")
i=0
y=10
for i in range(len(n)):
    n[i]=int(n[i])

i=0
for i in range(len(n)):
    if y == n[i]:
        print("found at index :",i)
        
print(n)