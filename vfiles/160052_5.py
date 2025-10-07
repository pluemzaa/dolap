i = 2
N = int(input("Enter a number N:"))
while i <= N:
    if i%2 == 0:
        if i==2:
            print(i)
        i = i+1
    elif i%3 == 0:
        if i == 3:
            print(i)
        i = i+1
    elif i%i ==0:
        print(i)
        i = i+1