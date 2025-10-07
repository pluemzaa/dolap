PetDict = {"Dog":0,"Cat":1,"Fish":2}
PetDict2 = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
Input = input("Enter your pets: ")
SepInput = Input.split(',')

print("Code of your pets: ",PetDict[SepInput[0]],",",PetDict[SepInput[1]],",",PetDict[SepInput[2]],",",PetDict[SepInput[3]],",",PetDict[SepInput[4]])
PetDict = {"Dog":0,"Cat":1,"Fish":2}
PetDict2 = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}

print("One-hot vectors:\n",PetDict2[SepInput[0]],"\n",PetDict2[SepInput[1]],"\n",PetDict2[SepInput[2]],"\n",PetDict2[SepInput[3]],"\n",PetDict2[SepInput[4]])