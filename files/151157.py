pet = input("Enter your pets: ")
pet = pet.split(',')
code = {
  'Dog': 0,
  'Cat': 1,
  'Fish': 2
}
ohv ={
  'Dog':[1,0,0],
  'Cat':[0,1,0],
  'Fish':[0,0,1]
}
code1 = code[pet[0]]
code2 = code[pet[1]]
code3 = code[pet[2]]
code4 = code[pet[3]]
code5 = code[pet[4]]
print(f"Code of your pets: {code1},{code2},{code3},{code4},{code5}")
ch1 = ohv[pet[0]]
ch2 = ohv[pet[1]]
ch3 = ohv[pet[2]]
ch4 = ohv[pet[3]]
ch5 = ohv[pet[4]]
print(f"One-hot vectors: \n{ch1}\n{ch2}\n{ch3}\n{ch4}\n{ch5}")