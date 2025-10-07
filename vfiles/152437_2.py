PET = input("Enter your pet: ")
PET1 = PET.split(" , ")
PET_CODE = {"Dog" :0,"Cat" :1,"Fish" :2}
print("Code of your pets: ",end="")
print(PET_CODE[PET1[0]] ,
      PET_CODE[PET1[1]] ,
      PET_CODE[PET1[2]] ,
      PET_CODE[PET1[3]] ,
      PET_CODE[PET1[4]] , sep=' , ')