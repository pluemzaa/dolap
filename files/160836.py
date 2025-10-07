Num = int(input('Enter the number of terms:'))
a= [0, 1]
i = 2
while i < Num:
    a.append(a[i-1]+a[i-2])
    i += 1
print(a)