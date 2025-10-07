v1 = input("Enter v1 (space-separated): ").split(" ")
v2 = input("Enter v2 (space-separated): ").split(" ")
for i in range (3):
  v1 = int(v1[i])
  v2 = int(v2[i])
sum = v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]
print (f"Dot product: {sum}")