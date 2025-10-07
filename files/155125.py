a = input("Enter a series of numbers separated by commas:")
b = a.split(",")
b[0] = int(b[0])
b[1] = int(b[1])
b[2] = int(b[2])
b[3] = int(b[3])
b[4] = int(b[4])
min_b = min(b)
max_b = max(b)
mxmi = max_b-min_b
c0 = (b[0]-min_b)/mxmi
c1 = (b[1]-min_b)/mxmi
c2 = (b[2]-min_b)/mxmi
c3 = (b[3]-min_b)/mxmi
c4 = (b[4]-min_b)/mxmi
print("Normalized values:")
print("%.2f" % c0)
print("%.2f" % c1)
print("%.2f" % c2)
print("%.2f" % c3)
print("%.2f" % c4)