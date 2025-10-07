x,y,z= map(int,input("Enter v1 (space-separated): ").split())
a,s,d= map(int,input("Enter v2 (space-separated): ").split())
vector = x*a+y*s+z*d
print(f"Dot product: {vector}")