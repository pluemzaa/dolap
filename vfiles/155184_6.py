lek = input("Enter a series of numbers separated by commas:")
set = lek.split(",")
set[0] = int(set[0])
set[1] = int(set[1])
set[2] = int(set[2])
set[3] = int(set[3])
set[4] = int(set[4])

min_x = min(set)
max_x = max(set)
print(min_x,max_x)

r0 = set[0] - min_x
r1 = set[1] - min_x
r2 = set[2] - min_x
r3 = set[3] - min_x
r4 = set[4] - min_x

print("Normalized values:")
print("%.2f" %r0)
print("%.2f" %r1)
print("%.2f" %r2)
print("%.2f" %r3)
print("%.2f" %r4)