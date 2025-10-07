n = input("Enter a series of numbers separated by commas: ")
n = n.split(",")
l = len(n)
for a in range(l):
    n[a] = int(n[a])

ma = max(n)
mi = min(n)
print("Normalized values:")
for i in range(l):
    xi = (n[i] - mi)/(ma-mi)
    print(f"{xi:.2f}")