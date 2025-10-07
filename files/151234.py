a = input("Enter your pets: ")
x = a.split(",")
p = {"Dog":0,"Cat":1,"Fish":2}
print(f"Code of your pets: {p[x[0]]},{p[x[1]]},{p[x[2]]},{p[x[3]]},{p[x[4]]}")

p = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
print(f"""One-hot vectors:
{p[x[0]]}
{p[x[1]]}
{p[x[2]]}
{p[x[3]]}
{p[x[4]]}
""")