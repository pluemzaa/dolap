s1 = int(input())
s2 = int(input())
s3 = int(input())
r = (s1*s2)/s3

if r%1 == 0:
    print(r)
else:
    r = ((s1*s2)//s3)+1
    print(r)