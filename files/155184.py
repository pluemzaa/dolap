lek = input("Enter a series of numbers separated by commas:")
set = lek.split(",")
set[0] = int(set[0])
set[1] = int(set[1])
set[2] = int(set[2])
set[3] = int(set[3])
set[4] = int(set[4])




r0 = (set[0] - min(set)) / (max(set)-min(set))
r1 = (set[1] - min(set)) / (max(set)-min(set))
r2 = (set[2] - min(set)) / (max(set)-min(set))
r3 = (set[3] - min(set)) / (max(set)-min(set))
r4 = (set[4] - min(set)) / (max(set)-min(set))



print("Normalized values:")
print("%.2f" %r0)
print("%.2f" %r1)
print("%.2f" %r2)
print("%.2f" %r3)
print("%.2f" %r4)