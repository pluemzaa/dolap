x=input("Enter a series of numbers separated by commas: ") 
xa=x.split(",") 
for xs in range(len(xa)):
    xa[xs]=int(xa[xs])
ma=max(xa) 
mn=min(xa)
io=len(xa) 
i=0
print('Normalized values:') 
while i<io:
    ko=(xa[i]-mn)/(ma-mn)   
    print(f"{ko:.2f}") 
    i+=1