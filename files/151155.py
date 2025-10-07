pe = input("Enter your pets: ")
ps = pe.split(',')
pd = {"Dog":0,"Cat":1,"Fish":2}
print(f"Code of your pets: {pd[ps[0]]},{pd[ps[1]]},{pd[ps[2]]},{pd[ps[3]]},{pd[ps[4]]}")

pd = {"Dog":[1, 0, 0],"Cat":[0, 1, 0],"Fish":[0, 0, 1]}
print(f"""One-hot vectors:
{pd[ps[0]]}
{pd[ps[1]]}
{pd[ps[2]]}
{pd[ps[3]]}
{pd[ps[4]]}
""")