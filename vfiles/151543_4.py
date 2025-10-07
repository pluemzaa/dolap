hname = {"Dog":0,"Cat":1,"Fish":2}
x = input("Enter your pets:")
pets = x.split()
a=(hname[pets[0]],hname[pets[1]],hname[pets[2]],hname[pets[3]],hname[pets[4]])
print(f"Code of your pets:{a}")