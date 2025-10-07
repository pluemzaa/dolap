a_str = input('Enter a:')
a = a_str.split(' ')
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])

print(a)

a = [1, 2, 3]
b = [5, 6, 7]

c0 = a[0] * b[0]
c1 = a[1] * b[1]
c2 = a[2] * b[2]

c = [c0, c1, c2]
print(c)
_sum = c0 + c1 + c2
print(_sum)