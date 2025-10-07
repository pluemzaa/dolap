n = int(input("Enter a number N: "))
for p in range(2,n+1):
    prime = True
    
    for i in range(2, p):
        if p % i == 0:
            prime = False  
            break       
    if prime:
        print(p)