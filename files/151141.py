v1 = list(map(int,input("Enter v1 (space-separated) : ").split()))
v2 = list(map(int,input("Enter v2 (space-separated) : ").split()))
dot_product = sum(x * y for x, y in zip(v1 , v2))
print("Dot product:" , dot_product)