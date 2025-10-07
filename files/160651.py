a = input("Enter a series of numbers separated by commas: ")
b = [float(c.strip()) for c in a.split(",")]
d = min(b)
e = max(b)
if e != d:
    f = [(g - d) / (e - d) for g in b]
else:
    f = [0.0 for _ in b]
print("Normalized values:")
for h in f:
    print(f"{h:.2f}")