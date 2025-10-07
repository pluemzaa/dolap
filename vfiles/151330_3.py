benz = input("Enter v1 (space-separated):")
enz = input("Enter v2 (space-separated):")

b1=benz.split(' ')
b2=enz.split(' ')

nee = (int(b1[0]) * int(b2[0]) * int(b1[1]) * int(b2[1]) * int(b1[2]) * int(b2[2]))
print("Dot product:",nee,end=' ')