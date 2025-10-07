tt = input("Enter v1 (space-separated): ")
ff = input("Enter v2 (space-separated): ")

b1 = tt.split(" ")
b2 = ff.split(" ")


if len(b1) < 3 or len(b2) < 3:
    print("Error: Both vectors must have at least 3 components for this calculation.")
else:
   
    pop = (int(b1[0]) * int(b2[0]) +
           int(b1[1]) * int(b2[1]) +
           int(b1[2]) * int(b2[2]))
    print("Dot product: ", pop, end=" ")