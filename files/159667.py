i = 2
while i <= N:
    p = 2
    prime = True

    while p < i:  
        if i % p == 0: 
            prime = False
            break
        p += 1 

    if prime:
        print(i)
    i += 1