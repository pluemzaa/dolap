PetDict = {"Dog":0,"Cat":1,"Fish":2}
Input = input("Enter your pets: ")
SepInput = Input.split(',')

print("Code of your pets: ",PetDict[SepInput[0]],",",PetDict[SepInput[1]],",",PetDict[SepInput[2]],",",PetDict[SepInput[3]],",",PetDict[SepInput[4]])