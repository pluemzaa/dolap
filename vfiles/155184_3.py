lek = int(input("Enter a series of numbers separated by commas:"))
set = lek.split(",")

x1 = x-min(x)
lob = max(x)- min(x)

min_x = min(lek)
max_x = max(lek)

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