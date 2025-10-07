a = input("Enter a series of numbers separated by commas: ")
a = a.split(",")

for i in range(0,len(a)):
    a[i] = int(a[i])

min_s = min(a)
max_s = max(a)
print("Normalized values:")
for i in range(len(a)):
    a_scaled = (a[i]-min_s) / (max_s - min_s)
    print(f"{a_scaled:.2f}")