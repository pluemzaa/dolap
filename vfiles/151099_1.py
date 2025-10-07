v1 = input("Enter v1 (space-separated): ").split(" ")
v2 = input("Enter v2 (space-separated): ").split(" ")
c = 0
g = 0
for i in range (3):
  v1 = int(v1[i])
  v2 = int(v2[i])
  c = g + (v1[i]*v2[i])
print (f"Dot product: {c}")