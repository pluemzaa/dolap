n=input("Enter numbers separated by commas: ")
y=int(input("Enter number to search: "))

n=n.split(",")
f=0
i=0
for  i in range(len(n)):
    if n[i] == y :
        print("found", y, "at index :",i)
        f= f+1

if f ==0:
    print("No",y,"found.")