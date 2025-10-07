N=int(input("Enter a number (enter 0 to stop):")) 
A=0
C=N
while N!=0:
    N=int(input("Enter a number (enter 0 to stop):")) 
    A+=1
    C=C+N
C=C/A
print(C)