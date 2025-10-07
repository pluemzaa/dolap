w = input("Enter a series of numbers separated by commas: ")
w = w.split(",")
for i in range(len(w)):
    w[i] = int(w[i])

min_ = min(w)
max_ = max(w)

print("Normalized values:")
for i in range(len(w)):
    normalized = (w[i] - min_) / (max_ - min_)
    print(f"{normalized:.2f}")