n=input("Enter numbers: ")
n=n.split(",")
#n_max=max(n)


for i in range(len(n)):
    n[i]=int(n[i])

n1=n[0]
for i in range(len(n)):
    if n[1] < n[i]:
        n1 =n[i]
        print("set the maximum value to ",n1)

print("The maximum value is:",n1)
#print(n_max)