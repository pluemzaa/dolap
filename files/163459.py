n=int(input(' '))
f=int(input(' '))
c=int(input(' '))

total=(n*f)/c
final=total-int(total)

if final==0:
    print(int(total))
elif final<1:
    print(int(total)+1)