hi = input("Enter a series of numbers separated by commas: ")
x = [float(i.strip())for i in hi.split(",")]
mi = min(x)
mx = max(x)
print("Normalized values:")
for v in x:
    hh = (v - mi)/(mx - mi)
    print("%.2f"%hh)