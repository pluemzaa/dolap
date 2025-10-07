a = input("Enter a series of numbers separated by commas:")
b = a.split(",")
c[0] = int(b[0])
c[1] = int(b[1])
c[2] = int(b[2])
c[3] = int(b[3])
min_c = min(c)
max_c = max(c)
d0 = c[0]-min_c
d1 = c[1]-min_c
d2 = c[2]-min_c
d3 = c[3]-min_c
print("%.2f" % d0)
print("%.2f" % d1)
print("%.2f" % d2)
print("%.2f" % d3)