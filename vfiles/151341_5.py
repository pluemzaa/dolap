v1_input=input('Enter v1 (space-separated): 1 2 3')
v1=[int(i)for i in v1_input.split()]
v2_input=input("Enter v2 (space-separated): 4 5 6")
v2=[int(i)for i in v2_input.split()]
dot_product=v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]
print(f"dot product: {dot_product}")