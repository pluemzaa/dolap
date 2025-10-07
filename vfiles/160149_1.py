n=input("Enter numbers separated by commas: ")
y=int(input("Enter number to search: "))
n=n.split(",")
i=0
while i < len(n):
    n[i]=int(n[i])
    i = i+1

i=0
while i< len (n):
    if y == n[i]:
        print("found at index :",i)
    i+= 1