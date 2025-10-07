pet = input("Enter your pets: ")
n5 = pet.split(",")
num = {"Dog": 0, "Cat": 1,"Fish": 2}
print("Code of your pets: ", end= " ")
print(num [n5[0]],
     num[n5[1]],
      num[n5[2]],
      num[n5[3]],
     num[n5[4]],sep=",")