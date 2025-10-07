numpet = {"Dog":0,"Cat":1,"Fish":2}
numpets = {"Dog":[1,0,0],"Cat":[0,1,0],"Fish":[0,0,1]}
cum = input("Enter your pets:")
cum1 = cum.split(",")
print("Code of your pets:",end='')
print(numpet[cum1[0]],
      numpet[cum1[1]],
      numpet[cum1[2]],
      numpet[cum1[3]],
      numpet[cum1[4]],sep=",")
cum2 = cum.split(",")
print("One-hot vectors:",end='\n')
print(numpets[cum2[0]],
      numpets[cum2[1]],
      numpets[cum2[2]],
      numpets[cum2[3]],
      numpets[cum2[4]],sep="\n")