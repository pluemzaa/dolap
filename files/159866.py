N=float(input("Enter a number (enter 0 to stop): ")) 
A=0
C=N
if N==0:
    print("No numbers entered.")
else:
    while N!=0:
     N=float(input("Enter a number (enter 0 to stop): ")) 
     A+=1
     C=C+N
     C=C/A
print("Average:",C)