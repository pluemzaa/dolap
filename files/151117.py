a_str = input("Enter v1 (space-separated): ")
a = a_str.split(' ')
b_str = input("Enter v2 (space-separated): ")
b = b_str.split(' ')

c0 = int(a[0]) * int(b[0])
c1 = int(a[1]) * int(b[1])
c2 = int(a[2]) * int(b[2])

_sum = c0 + c1 + c2

print(f"Dot product: {_sum}")