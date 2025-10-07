p1 = input("Enter your pets: ")
p2 = p1.split(',')
p3 = {"Dog":0,"Cat":1,"Fish":2} 
print(f"Code of your pets: {p3[p2[0]]},{p3[p2[1]]},{p3[p2[2]]},{p3[p2[3]]},{p3[p2[4]]}")
p3 = {"Dog":	[1, 0, 0],"Cat":	[0, 1, 0],"Fish":	[0, 0, 1]} 
print(f"""One-hot vectors:
{p3[p2[0]]}
{p3[p2[1]]}
{p3[p2[2]]}
{p3[p2[3]]}
{p3[p2[4]]}""")