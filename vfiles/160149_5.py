n=input("Enter numbers separated by commas: ")
y=input("Enter number to search: ")
n=n.split(",")
f=0
i=0
while i< len (n):
    if y == n[i]:
        print("found", y, "at index :",i)
    i = i+1
    f= f+1
if f ==0:
    print("No",y,"found.")