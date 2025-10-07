ani = {"Dog": 0, "Cat": 1, "Fish": 2}
onehot = {"Dog": "[1, 0, 0]", "Cat": "[0, 1, 0]", "Fish": "[0, 0, 1]"}

pet1 = input().strip()
pet2 = input().strip()
pet3 = input().strip()
pet4 = input().strip()
pet5 = input().strip()

print("Code of your pets:", str(ani[pet1]) + "," + str(ani[pet2]) + "," + str(ani[pet3]) + "," + str(ani[pet4]) + "," + str(ani[pet5]))
print("One-hot vectors:")
print(onehot[pet1])
print(onehot[pet2])
print(onehot[pet3])
print(onehot[pet4])
print(onehot[pet5])