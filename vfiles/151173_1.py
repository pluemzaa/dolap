a = input("Enter your pets: ")
pet = {"Dog":0,"Cat":1,"Fish":2}
pet2 = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
pets = a.split(",")
c0 = pet[pets[0]]
c1 = pet[pets[1]]
c2 = pet[pets[2]]
c3 = pet[pets[3]]
c4 = pet[pets[4]]

r0 = pet2[pets[0]]
r1 = pet2[pets[1]]
r2 = pet2[pets[2]]
r3 = pet2[pets[3]]
r4 = pet2[pets[4]]
C = str(c0), str(c1), str(c2), str(c3), str(c4)
print(f"Code of your pets: {c0},{c1},{c2},{c3},{c4}")
print(f"One-hot vectors: {r0}{r1}{r2}{r3}{r4}")