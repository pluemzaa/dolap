n = 2
for i in range(n):
    for j in range(i*2):
        print('**' ,end='')
    print()
    if n < 1:
        print("Error number must be 1 or greater")