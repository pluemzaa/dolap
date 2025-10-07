s1 = int(input())
s2 = int(input())
s3 = int(input())
total1 = s1*s2
if total1 % s3 == 0:
    total = int(s1*s2/s3)
else:
    total = int((s1*s2/s3))+1
print(total)