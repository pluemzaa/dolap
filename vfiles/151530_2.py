pets = input("Enter your pets: ").split(',')
pet = {"Dog" : 0,"Cat" : 1,"Fish" : 2}
vec = {"Dog" : [1,0,0],"Cat" : [0,1,0],"Fish" : [0,0,1]}
print(f"Code of your pets: {pet[pets[0]]},{pet[pets[1]]},{pet[pets[2]]},{pet[pets[3]]},{pet[pets[4]]}")
print(f"One-hot vectors: ",f"{vec[pets[0]]},{vec[pets[1]]},{vec[pets[2]]},{vec[pets[3]]},{vec[pets[4]]}",sep='\n')