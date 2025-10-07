hhhh = {"Dog":0,"Cat":1,"Fish":2}
hname = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
x = input("Enter your pets: ")
pets = x.split(',')
print("Code of your pets:",end=" ")
a = (hhhh[pets[0]],hhhh[pets[1]],hhhh[pets[2]],hhhh[pets[3]],hhhh[pets[4]])
print(f'{a}')
print('One-hot vectors:',end='\n')
print(hname[pets[0]],hname[pets[1]],hname[pets[2]],hname[pets[3]],hname[pets[4]],sep='\n')