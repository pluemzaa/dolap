tt = input("Enter v1 (space-separated): ")
ff = input("Enter v2 (space-separated): ")

b1=tt.split(" ")
b2=ff.split(" ")

pop = (int(b1[0])  * int(b2[0]) +  int(b1[0]) * int(b2[0])+  int(b1[0]) * int(b2[0]))
print("Dot product: ",pop,end=" ")