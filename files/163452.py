l1 = int(input())
l2 = int(input())
l3 = int(input())

r = (l1*l2)/l3

print(r if r % 1 == 0 else (l1*l2) // l3 + 1 )